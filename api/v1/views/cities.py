#!/usr/bin/python3
""" objects that handles all default RestFul API actions for cities """
from models.city import City
from models.state import State
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from


@app_views.route('/states/<state_id>/cities', methods=['GET'],
                 strict_slashes=False)
@swag_from('documentation/city/cities_by_state.yml', methods=['GET'])
@cities_bp.route('/states/<state_id>/cities', methods=['GET'])
def get_cities_by_state(state_id):
    state = State.query.get(state_id)
    if not state:
        abort(404)
    cities = City.query.filter_by(state_id=state_id).all()
    return jsonify([city.to_dict() for city in cities])

@cities_bp.route('/cities/<city_id>', methods=['GET'])
def get_city(city_id):
    city = City.query.get(city_id)
    if not city:
        abort(404)
    return jsonify(city.to_dict())

@cities_bp.route('/cities/<city_id>', methods=['DELETE'])
def delete_city(city_id):
    city = City.query.get(city_id)
    if not city:
        abort(404)
    db.session.delete(city)
    db.session.commit()
    return jsonify({}), 200

@cities_bp.route('/states/<state_id>/cities', methods=['POST'])
def create_city(state_id):
    state = State.query.get(state_id)
    if not state:
        abort(404)
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    if 'name' not in data:
        abort(400, 'Missing name')
    city = City(name=data['name'], state_id=state_id)
    db.session.add(city)
    db.session.commit()
    return jsonify(city.to_dict()), 201

@cities_bp.route('/cities/<city_id>', methods=['PUT'])
def update_city(city_id):
    city = City.query.get(city_id)
    if not city:
        abort(404)
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    for key, value in data.items():
        if key not in ['id', 'state_id', 'created_at', 'updated_at']:
            setattr(city, key, value)
    db.session.commit()
    return jsonify(city.to_dict()), 200
