from flask import Flask, request, render_template
from flask.json import jsonify
from app import app
from user.models import Usuarios

@app.route('/usuario/sair/')
def sair():
    return Usuarios().sair()

@app.route('/logar', methods=['POST'])
def logar():
    return Usuarios().logar()

@app.route('/senha')
def senha():
    return Usuarios().gerarSenha()

@app.route('/naologado')
def naologado():
    return render_template('nlogado.html')

# db.usuarios.insert({"_id":5,"nome":"teste","senha":"$pbkdf2-sha256$29000$WouR8j7nnLNWyrk3BkBorQ$JfCtGjjpzj/bwSHK95od7/KfcUCvfLjEsKW8yaNER7A"})