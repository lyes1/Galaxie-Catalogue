# coding: utf-8
#
from flask import Flask, render_template, request, json, jsonify
from . import routes
from utils import retrieve_all, retrieve_spec


@routes.route('/api/celestialObjetcs/results', methods=['GET'])
def results(name=None):
    # Lecture des paramètres
    query_parameters = request.args

    catalogue = query_parameters.get('cat')
    scope = query_parameters.get('scope')
    objNum = query_parameters.get('objNum')
    NGCDes = query_parameters.get('NGCDes')
    Const = query_parameters.get('Const')

    print( (catalogue, scope,objNum, NGCDes, Const))

    all_cat_objects = {}

    if (scope=="all"):
        all_cat_objects = retrieve_all(catalogue)
    else: # scope=spec
        all_cat_objects = retrieve_spec(catalogue, objNum, NGCDes, Const)

    # Saving the order of the columns after the jsonifying process
    results = []
    if (len(all_cat_objects)!=0):
        keys = list(all_cat_objects[0].keys())
        results.append(keys)
        results.append(all_cat_objects)  
    return jsonify(results)

