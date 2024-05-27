#!/usr/bin/python3

""" index route """

from api.v1.views import app_views
from flask import jsonify


@app_views.route("/status", strict_slashes=False)
def index():
    """Returns a JSON object with the status of the API"""
    return jsonify({"status": "OK"})


@app_views.route("/stats", strict_slashes=False)
def stats():
    """retrieves the number of each objects by type"""
    from models.user import User

    stats = {}
    stats["users"] = User.count()
    return jsonify(stats)
