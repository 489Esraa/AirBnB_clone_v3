#!/usr/bin/python3

"""Endpoint route will be to return the status of your API"""

from flask import Flask 
from api.v1.views import app_views
from models import storage
import os

#the instance of flask
app = Flask(__name__)

app.register_blueprint(app_views, url_prefix="/api/v1")

if __name__ == "__main__":
    if os.getnev("HBNB_API_HOST"):
        API_HOST = os.getnev("HBNB_API_HOST")
    else:
        API_HOST = "0.0.0.0"
        
    if os.getnev("HBNB_API_PORT"):
        API_PORT = int(os.getnev("HBNB_API_PORT"))
    else:
        API_PORT = 5000
    app.run(host=API_HOST, port=API_PORT, threaded=True)