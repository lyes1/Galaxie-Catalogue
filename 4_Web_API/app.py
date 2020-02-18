# coding: utf-8
'''
Point d'entrer de l'application
'''

# Les imports
from routes import routes, page_not_found
from flask import Flask, render_template, request, json, jsonify

app = Flask(__name__)

# A supprimer lors du déploiement
app.config["DEBUG"] = True

# Les routes sont définies dans le module routes
# Réference du code https://stackoverflow.com/questions/15231359/split-python-flask-app-into-multiple-files
app.register_blueprint(routes)
app.register_error_handler(404, page_not_found)

if __name__=="__main__":
    # Lancement du serveur
    app.run()      
