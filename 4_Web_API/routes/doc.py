from flask import Flask, render_template, request, json, jsonify
from . import routes

@routes.route('/doc', methods=['GET'])
def signUp():
    return render_template('/doc.html')
