from flask import Flask
from app import app
from user.models import Usuarios

@app.route('/usuario/sair')
def sair():
    # return "oi"
    return Usuarios().sair()
@app.route('/logar')
def logar():
    return Usuarios().logar()