from flask import Flask, redirect, url_for, render_template, session
import pandas as pd
import pymongo


app = Flask(__name__, template_folder='./templates')
app.secret_key = b'\xf5\xdc\xf6\xa7\x06\xb1\x11U\xe3\x18\xd0C\xde\xf9<\xd2'

client = pymongo.MongoClient('localhost',27017) 
db = client.login

from user import routes 
from estado import routes 

@app.route('/')
def login():
    return render_template("login.html")

@app.route('/dashboard/')
def dashboard():
    if 'logado' in session:
        return render_template('dashboard.html')
    else:
        return redirect('/')