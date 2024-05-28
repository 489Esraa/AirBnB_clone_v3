#!/usr/bin/python3

"""Endpoint route will be to return the status of your API"""

from flask import Flask
from api.v1.views import app_views
from models import storage
import os
from flask import jsonify
from flask_cors import CORS


#the instance of flask
app = Flask(__name__)

app.register_blueprint(app_views, url_prefix="/api/v1")

if __name__ == "__main__":
    if os.getenv("HBNB_API_HOST"):
        API_HOST = os.getenv("HBNB_API_HOST")
    else:
        API_HOST = "0.0.0.0"

    if os.getenv("HBNB_API_PORT"):
        API_PORT = int(os.getenv("HBNB_API_PORT"))
    else:
        API_PORT = "5000"
    app.run(host=API_HOST, port=API_PORT, threaded=True)

CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})

app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """ returns 404 Error """
    return jsonify({"error": "Not found"}), 404
