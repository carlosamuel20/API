import re
from flask import Flask, redirect, session
from app import app
from estado.models import Estado

@app.route('/estados/pobres')
def estados_pobres():
    if 'logado' in session:
        return Estado().listarPobres()
    else:
        return redirect('/naologado')

@app.route('/estados/ricos')
def estados_ricos():
    if 'logado' in session:
       return Estado().listarRicos()
    else:
        return redirect('/naologado')
    