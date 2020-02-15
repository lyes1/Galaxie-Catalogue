from flask import Flask, render_template, request, json, jsonify, redirect, url_for
from . import routes

@routes.route('/')
def api_landing():
        return redirect('/api/celestialObjetcs', code=302)

@routes.route('/api/celestialObjetcs', methods=['GET', 'POST'])
def api():
    return render_template('api.html')

@routes.route('/api/doc')
def doc():
    return render_template('doc.html')

@routes.route('/api/about')
def about():
    return render_template('about.html')
