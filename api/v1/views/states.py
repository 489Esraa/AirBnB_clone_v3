#!/usr/bin/python3

"""States route """

from flask import jsonify, request
from models import storage
from models.state import State
from api.v1.views import app_views


@app_views.route("/states", methods=["GET"], strict_slashes=False)
def states():
    """Retrieves the list of all State objects"""
    states = storage.all(State)
    return jsonify([state.to_dict() for state in states.values()])


@app_views.route("/states/<state_id>", methods=["GET"], strict_slashes=False)
def state(state_id):
    """Retrieves a State object"""
    state = storage.get(State, state_id)
    if state is None:
        return jsonify({"error": "Not found"}), 404
    return jsonify(state.to_dict())


@app_views.route("/states/<state_id>", methods=["DELETE"], strict_slashes=False)
def delete_state(state_id):
    """Deletes a State object"""
    state = storage.get(State, state_id)
    if state is None:
        return jsonify({"error": "Not found"}), 404
    state.delete()
    storage.save()
    return jsonify({})


@app_views.route("/states", methods=["POST"], strict_slashes=False)
def create_state():
    """Creates a State object"""
    if not request.get_json():
        return jsonify({"error": "Not a JSON"}), 400
    if "name" not in request.get_json():
        return jsonify({"error": "Missing name"}), 400
    state = State(**request.get_json())
    state.save()
    return jsonify(state.to_dict()), 201


@app_views.route("/states/<state_id>", methods=["PUT"], strict_slashes=False)
def update_state(state_id):
    """Updates a State object"""
    state = storage.get(State, state_id)
    if state is None:
        return jsonify({"error": "Not found"}), 404
    if not request.get_json():
        return jsonify({"error": "Not a JSON"}), 400
    for key, value in request.get_json().items():
        if key not in ["id", "created_at", "updated_at"]:
            setattr(state, key, value)
    storage.save()
    return jsonify(state.to_dict())
