#!/usr/bin/python3
""""""
from flask import jsonify  # Add this import statement
from api.v1.views import app_views


@app_views.route('/status', strict_slashes=False)
def status():
    """Returns a JSON"""
    return jsonify({"status": "OK"})
