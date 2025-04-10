from cryptography.fernet import Fernet
from flask import Flask, render_template

app = Flask(__name__)

# Génération de la clé (valable pour la session du serveur)
key = Fernet.generate_key()
f = Fernet(key)

@app.route('/')
def hello_world():
    return render_template('hello.html')  #commit

# Route Encrypt : chiffre une valeur
@app.route('/encrypt/<string:valeur>')
def encryptage(valeur):
    valeur_bytes = valeur.encode()  # str -> bytes
    token = f.encrypt(valeur_bytes)  # Encrypt
    return f"Valeur encryptée : {token.decode()}"  # bytes -> str

# Route Decrypt : déchiffre un token
@app.route('/decrypt/<string:token>')
def decryptage(token):
    token_bytes = token.encode()  # str -> bytes
    valeur = f.decrypt(token_bytes)  # Decrypt
    return f"Valeur décryptée : {valeur.decode()}"  # bytes -> str

if __name__ == "__main__":
    app.run(debug=True)
