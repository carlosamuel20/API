from flask import Flask, jsonify, request, session, redirect, url_for 
from passlib.hash import pbkdf2_sha256 
from app import db 
import uuid 
 
 
class Usuarios: 
    usuario = { 
        '_id': '', 
        'nome': '', 
        'senha': '' 
    } 
     
    def iniciar_sessao(self, usuario): 
        session['logado'] = True 
        session['usuario'] = usuario 
         
    def logar(self): 
        usuario = db.usuarios.find_one({ 
            'nome': request.form['nome'] 
        }) 
        if usuario and pbkdf2_sha256.verify(request.form['senha'], usuario['senha']): 
            self.iniciar_sessao(usuario) 
            return redirect(url_for('dashboard')) 
        else: 
            return jsonify({'error':'Invalid login credentials'}, usuario, pbkdf2_sha256.encrypt(request.form['senha']) ), 401
     
    def sair(self): 
        return jsonify(self.usuario)

    def sair(self):
        session.clear()
        return redirect('/naologado')

        # {"_id":"2","nome":"teste","senha":"$pbkdf2-sha256$29000$htAaw3iP8b6Xcq71npNyTg$bAoJeyDeuAxyGrSHqnkfIefRlcqYaIB1wGG2vEXrEIA"},"$pbkdf2-sha256$29000$XmsNASCktJbS.h9DyBlDiA$ZC8itMx.vhWQZVE11rSvsv4mGC7ssiRfGTY.nmpqjHA"]