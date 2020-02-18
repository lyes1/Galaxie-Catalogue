# coding: utf-8
#
from routes import routes
from flask import Flask, render_template, request, json, jsonify
import os

app = Flask(__name__)
app.config["DEBUG"] = True # delete

# Les routes sont définies dans le dossier routes
# Ref https://stackoverflow.com/questions/15231359/split-python-flask-app-into-multiple-files
app.register_blueprint(routes)

if __name__=="__main__":
    app.run()      
