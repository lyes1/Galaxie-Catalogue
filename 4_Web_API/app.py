# coding: utf-8
#
#from routes import models
from routes import *
from flask import Flask, render_template, request, json, jsonify
import os
import sqlite3
#import models

app = Flask(__name__)
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
    db = models.connectionDatabase()
    print(models.select_object(db, "Messier", "M1"))
    app.run()      
