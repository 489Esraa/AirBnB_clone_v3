#!/usr/bin/python3

"""States route """

from flask import jsonify, request, make_response
from models import storage
from models.state import State
from api.v1.views import app_views


@app_views.route("/states", methods=["GET"], strict_slashes=False)
def get_states():
    """
    Retrieves the list of all State objects
    """
    all_states = storage.all(State).values()
    list_states = []
    for state in all_states:
        list_states.append(state.to_dict())
    return jsonify(list_states)


@app_views.route("/states/<state_id>", methods=["GET"], strict_slashes=False)
def state(state_id):
    """Retrieves a State object"""
    state = storage.get(State, state_id)
    if state is None:
        return jsonify({"error": "Not found"}), 404
    return jsonify(state.to_dict())


@app_views.route(
    "/states/<state_id>", methods=["DELETE"], strict_slashes=False
    )
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
def put_state(state_id):
    """Updates a State object"""
    state = storage.get(State, state_id)
    if state is None:
        return jsonify({"error": "Not found"}), 404
    if not request.get_json():
        return jsonify({"error": "Not a JSON"}), 400
    ignore = ['id', 'created_at', 'updated_at']

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(state, key, value)
    storage.save()
    return make_response(jsonify(state.to_dict()), 200)
