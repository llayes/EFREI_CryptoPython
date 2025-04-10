from cryptography.fernet import Fernet
from flask import Flask, render_template

app = Flask(__name__)

# Clé générée UNE FOIS (fixe)
key = b'RJ0aaTGn9w5EYIDUkf1ogd81MizG5XoKL5S6Z70PuQA='  # Exemple de clé générée
f = Fernet(key)

@app.route('/')
def hello_world():
    return render_template('hello.html')

# Afficher la clé (bonus)
@app.route('/key')
def show_key():
    return f"Clé utilisée : {key.decode()}"

@app.route('/encrypt/<string:valeur>')
def encryptage(valeur):
    valeur_bytes = valeur.encode()
    token = f.encrypt(valeur_bytes)
    return f"Valeur encryptée : {token.decode()}"

@app.route('/decrypt/<string:token>')
def decryptage(token):
    token_bytes = token.encode()
    valeur = f.decrypt(token_bytes)
    return f"Valeur décryptée : {valeur.decode()}"

if __name__ == "__main__":
    app.run(debug=True)
