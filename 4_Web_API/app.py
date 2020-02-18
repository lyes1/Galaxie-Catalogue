# coding: utf-8
#
from routes import routes, page_not_found
from flask import Flask, render_template, request, json, jsonify
import os

app = Flask(__name__)
app.config["DEBUG"] = True # delete

# Les routes sont définies dans le dossier routes
# Ref https://stackoverflow.com/questions/15231359/split-python-flask-app-into-multiple-files
app.register_blueprint(routes)
app.register_error_handler(404, page_not_found)

if __name__=="__main__":
    app.run()      
