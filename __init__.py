from cryptography.fernet import Fernet
from flask import Flask, render_template

app = Flask(__name__)

# Page d'accueil
@app.route('/')
def hello_world():
    return render_template('hello.html')

# Génération d'une clé Fernet
@app.route('/generate_key')
def generate_key():
    key = Fernet.generate_key()
    return f"Voici ta clé : {key.decode()}"

# Encrypt avec la clé du serveur (classique)
@app.route('/encrypt/<string:valeur>')
def encryptage(valeur):
    key = Fernet.generate_key()  # Générer une clé unique
    f = Fernet(key)
    valeur_bytes = valeur.encode()
    token = f.encrypt(valeur_bytes)
    return f"Clé : {key.decode()} | Valeur encryptée : {token.decode()}"

# Décryptage avec clé + token fournis par l'utilisateur
@app.route('/decrypt/<string:cle>/<path:token>')
def decryptage(cle, token):
    try:
        f = Fernet(cle.encode())
        token_bytes = token.encode()
        valeur = f.decrypt(token_bytes)
        return f"Valeur décryptée : {valeur.decode()}"
    except Exception as e:
        return f"Erreur lors du décryptage : {e}"

if __name__ == "__main__":
    app.run(debug=True)
