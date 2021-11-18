from flask import Flask, redirect, url_for, render_template
import pandas as pd
import pymongo


# df = pd.read_csv('vw_pib_percapita.csv',encoding='iso-8859-1',delimiter =',')

app = Flask(__name__, template_folder='./templates')

client = pymongo.MongoClient('localhost',27017) 
db = client.login
from user import routes 

@app.route('/')
def login():
    return render_template("login.html")