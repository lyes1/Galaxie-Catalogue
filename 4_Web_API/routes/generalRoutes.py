# coding: utf-8
'''
Définitions des routes générales de notre site
'''

# Les import
from flask import Flask, render_template, request, json, jsonify, redirect, url_for
from . import routes

@routes.errorhandler(404)
def page_not_found(e):
    '''
    La page à renvoyer en cas d'une URL inéxistante
    '''
    return render_template('404.html'), 404

@routes.route('/')
def api_landing():
    '''
    Redirection vers la page de l'API
    '''
        return redirect('/api/celestialObjetcs', code=302)

@routes.route('/api/celestialObjetcs', methods=['GET', 'POST'])
def api():
    '''
    Route vers l'API
    '''
    return render_template('api.html')

@routes.route('/api/doc')
def doc():
    '''
     Route vers la page docummentation
    '''
    return render_template('documentation.html')

# 
@routes.route('/api/about')
def about():
    '''
    Route vers la page About
    '''
    return render_template('about.html')


