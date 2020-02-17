from flask import request, jsonify
from flask import render_template
import sqlite3
#
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''


@app.route('/api/v1/resources/celestialObjetcs', methods=['GET'])
def api_all():
    query_parameters = request.args
    cat = query_parameters.get('cat')
    conn = sqlite3.connect(database_path)
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_cat_objects = cur.execute('SELECT * FROM '+cat+';').fetchall()

    #return jsonify(all_cat_objects)
    return render_template('layouts/base.html', title='Result', objects=all_cat_objects)

@app.route('/api/v1/resources/celestialObjetcs', methods=['GET'])
def api_filter():
    query_parameters = request.args

    id = query_parameters.get('id')
    published = query_parameters.get('published')
    author = query_parameters.get('author')

    query = "SELECT * FROM books WHERE"
    to_filter = []

    if id:
        query += ' id=? AND'
        to_filter.append(id)
    if published:
        query += ' published=? AND'
        to_filter.append(published)
    if author:
        query += ' author=? AND'
        to_filter.append(author)
    if not (id or published or author):
        return page_not_found(404)

    query = query[:-4] + ';'

    conn = sqlite3.connect('books.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    results = cur.execute(query, to_filter).fetchall()

    return jsonify(results)
