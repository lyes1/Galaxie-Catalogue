# coding: utf-8
#
from flask import Flask, render_template, request, json, jsonify
from . import routes
import sqlite3
from pony.orm import db_session
import os

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def retrieve_all(catalogue):
    database_path = os.path.join("..", "3_Database_creation", "cataloqueSqlite.db")
    conn = sqlite3.connect(database_path)
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_cat_objects = cur.execute('SELECT * FROM '+catalogue+';').fetchall()
    return all_cat_objects

def retrieve_spec(catalogue, objNum, NGCDes, Const):
    database_path = os.path.join("..", "3_Database_creation", "cataloqueSqlite.db")
    conn = sqlite3.connect(database_path)
    conn.row_factory = dict_factory
    cur = conn.cursor()

    if (objNum!=''):
        if (catalogue=="Messier"):
            return cur.execute("SELECT * FROM "+catalogue+" WHERE Messier_number = '" +objNum+ "';").fetchall()
        elif (catalogue=="Caldwell"):
            return cur.execute("SELECT * FROM "+catalogue+" WHERE Caldwell_number ='" +objNum+ "';").fetchall()
        else: #catalogue=="Herschel400"
            return cur.execute("SELECT * FROM "+catalogue+" WHERE NGC_designation = '" + objNum+ "';").fetchall()
    elif (Const!=''):
            return cur.execute("SELECT * FROM "+catalogue+" WHERE Constellation_Latin = '" + Const+ "';").fetchall()
    elif (NGCDes!=''):
        if (catalogue=="Herschel400"):
             return cur.execute("SELECT * FROM " +catalogue+" WHERE NGC_designation = '" + NGCDes+ "';").fetchall()
        else: # Messier or Caldwell
             return cur.execute("SELECT * FROM "+catalogue+" WHERE NGC_IC_designation = '" +NGCDes+ "';").fetchall()
    else:
         return {}
    ##all_cat_objects = cur.execute('SELECT * FROM '+catalogue+';').fetchall()
    ##return {}

@routes.route('/api/celestialObjetcs/results', methods=['GET'])
@db_session
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
    #query_parameters = request.args
    #cat = query_parameters.get('cat')
    #print (database_path)
    #database_path = os.path.join("..", "3_Database_creation", "cataloqueSqlite.db")
    #conn = sqlite3.connect(database_path)
    #conn.row_factory = dict_factory
    #cur = conn.cursor()
    #all_cat_objects = cur.execute('SELECT * FROM '+catalogue+';').fetchall()
    
    # Saving the order of the columns after the jsonifying process
    results = []
    if (len(all_cat_objects)!=0):
        keys = list(all_cat_objects[0].keys())
        results.append(keys)
        results.append(all_cat_objects)  
    return jsonify(results)
    #return jsonify([])


