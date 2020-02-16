from flask import Flask, render_template, request, json, jsonify
from . import routes

import sqlite3
import os
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d



@routes.route('/api/celestialObjetcs/results', methods=['GET'])
def results(name=None):
    query_parameters = request.args

    username = query_parameters.get('username')
    print(username)
    password= query_parameters.get('passs')
    print(password)

    database_path = os.path.join("..", "3_Database_creation", "cataloqueSqlite.db")
    query_parameters = request.args
    cat = query_parameters.get('cat')
    print (database_path)

    conn = sqlite3.connect(database_path)
    conn.row_factory = dict_factory
    cur = conn.cursor()
    cat = "Messier"
    all_cat_objects = cur.execute('SELECT * FROM '+cat+';').fetchall()
    
    # Saving the order of the columns after the jsonifying process
    results = []
    if (len(all_cat_objects)!=0):
        keys = list(all_cat_objects[0].keys())
        results.append(keys)
        results.append(all_cat_objects)  
    return jsonify(results)
    #return jsonify([])