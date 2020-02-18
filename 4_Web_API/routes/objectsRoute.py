# coding: utf-8
'''
Définition de route vers la page API
'''
from flask import Flask, render_template, request, json, jsonify
from . import routes
from utils import retrieve_all, retrieve_spec

# La route vers la page API
@routes.route('/api/celestialObjetcs/results', methods=['GET'])
def results(name=None):

    # Lecture des paramètres
    query_parameters = request.args

    catalogue = query_parameters.get('cat') # Nom du catalogue
    scope = query_parameters.get('scope') # all objects of the catalogue or specific ones
    objNum = query_parameters.get('objNum') # Numero de l'objet Messier/Caldwell/NGC (pour Hershel400)
    NGCDes = query_parameters.get('NGCDes') # Désignation NGC/IC de l'objet
    Const = query_parameters.get('Const') # Constellation

    all_cat_objects = {}

    # Récupérer tous les objets du catalogue
    if (scope=="all"):
        all_cat_objects = retrieve_all(catalogue)
    else: # scope=spec, récupérer des objets spécifiques
        all_cat_objects = retrieve_spec(catalogue, objNum, NGCDes, Const)

    # Saving the order of the columns after the jsonifying process
    results = []
    if (len(all_cat_objects)!=0):
        keys = list(all_cat_objects[0].keys())
        results.append(keys)
        results.append(all_cat_objects)  
    return jsonify(results)

