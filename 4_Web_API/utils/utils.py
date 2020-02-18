# coding: utf-8
#
import sqlite3
import os

database_path = os.path.join("..", "3_Database_creation", "cataloqueSqlite.db")

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def retrieve_all(catalogue):
    conn = sqlite3.connect(database_path)
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_cat_objects = cur.execute('SELECT * FROM '+catalogue+';').fetchall()
    return all_cat_objects

def retrieve_spec(catalogue, objNum, NGCDes, Const):
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
