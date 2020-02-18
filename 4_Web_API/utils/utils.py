# coding: utf-8
'''
Définitions des méthodes permettant d'exécuter les requêtes SQL
'''

import sqlite3
import os

# Chemin vers la base de données
database_path = os.path.join("..", "3_Database_creation", "cataloqueSqlite.db")

def dict_factory(cursor, row):
    '''
    configuration de la connexion
    '''
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def retrieve_all(catalogue):
    '''
    Récupérer tous les objets d'une table
    Param : catalogue
    return : Objects
    '''
    conn = sqlite3.connect(database_path)
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_cat_objects = cur.execute('SELECT * FROM '+catalogue+';').fetchall()
    return all_cat_objects

def retrieve_spec(catalogue, objNum, NGCDes, Const):
    '''
    Récupérer des objets spécifiques
    Param : catalogue (Nom du catalogue), objNum (Numero de l'objet Messier/Caldwell/NGC (pour Hershel400)), NGCDes(Désignation NGC/IC de l'objet), Const(Constellation)
    return : Objects
    '''
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
