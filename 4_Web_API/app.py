# coding: utf-8
#
#from routes import models
from routes import *
from flask import Flask, render_template, request, json, jsonify
import os
from pony.flask import Pony
import sqlite3
#from models import db

app = Flask(__name__)
#Pony(app)
app.config["DEBUG"] = True # delete

# Les routes sont définies dans le dossier routes
# Ref https://stackoverflow.com/questions/15231359/split-python-flask-app-into-multiple-files
app.register_blueprint(routes)

def dict_factory1(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

if __name__=="__main__":

    # Connexion de l'objet database à la base de donnée 'cataloqueSqlite
    database_path = os.path.join("..", "3_Database_creation", "cataloqueSqlite.db")
    db.bind('sqlite', database_path, create_db=True)
    #set_sql_debug(True)

    # Connexion des entities aux tables de la base de données 'cataloqueSqlite'
    db.generate_mapping(create_tables=True)

    #db = models.connectionDatabase()
   # print(models.select_object(db, "Messier", "M1"))
    app.run()      
