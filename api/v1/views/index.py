#!/usr/bin/python3
"""Create app_views instance"""

from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


@app_views.route("/status", strict_slashes=False)
def index():
    """Returns a JSON object with the status of the API"""
    return jsonify({"status": "OK"})


@app_views.route("/stats", strict_slashes=False)
def stats():
    """retrieves the number of each objects by type"""
    hbnbclasses = {
        "amenities": "Amenity",
        "cities": "City",
        "places": "Place",
        "reviews": "Review",
        "states": "State",
        "users": "User",
    }
    dict_count = {}
    for k, v in hbnbclasses.items():
        dict_count[k] = storage.count(v)
    return jsonify(dict_count)
