# coding: utf-8
#
from flask import Flask, render_template, request, json, jsonify, redirect, url_for
from . import routes

@routes.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

#Redirection vers la page de l'API
@routes.route('/')
def api_landing():
        return redirect('/api/celestialObjetcs', code=302)

@routes.route('/')
@routes.route('/api/celestialObjetcs', methods=['GET', 'POST'])
def api():
    return render_template('api.html')

@routes.route('/api/doc')
def doc():
    return render_template('documentation.html')

@routes.route('/api/about')
def about():
    return render_template('about.html')


