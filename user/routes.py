import re
from flask import Flask, request, render_template, request
from flask.json import jsonify
from app import app
from user.models import Usuarios

@app.route('/sair/')
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

@app.route('/cadastrar', methods=['POST', 'GET'])
def cadastrar():
    if request.method == 'POST':
        return Usuarios().cadastrar()
    else:
        return render_template('cadastrar.html')


