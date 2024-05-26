#!/usr/bin/python3

from api.v1.views import app_views
from flask import jsonify


@app_views.route("/status", strict_slashes=False)
def index():
    """Returns a JSON object"""
    return jsonify({"status": "OK"})


@app_views.route("/stats", strict_slashes=False)
def stats():
    """Returns a JSON object"""
    from models.user import User

    stats = {}
    stats["users"] = User.count()
    return jsonify(stats)
