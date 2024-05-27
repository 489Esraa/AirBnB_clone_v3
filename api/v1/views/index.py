#!/usr/bin/python3

"""create app_views instance"""
from api.v1.views import app_views
from flask import jsonify

@app_views.route('/status', strict_slashes=False)
def app_status():
    """payload that will return when
    this route is call return status with json
    """
    result = {"status": "OK"}
    return jsonify(result), 200