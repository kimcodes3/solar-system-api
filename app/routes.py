from flask import Blueprint, jsonify, request
from .models.planet import Planet
from app import db

planet_bp = Blueprint("planet", __name__, url_prefix="/planet")

@planet_bp.route("", methods=["GET"])
def get_planets():
    response = []
    all_planets = Planet.query.all()
    for planet in all_planets:
        response.append(planet.get_dict())
    return jsonify(response), 200

@planet_bp.route("", methods=["POST"])
def add_one_planet():
    request_body = request.get_json()
    new_planet = Planet(
        name = request_body["name"], 
        description = request_body["description"],
        position = request_body["position"],
        )
    db.session.add(new_planet)
    db.session.commit()

    return {"id": new_planet.id}, 201

# @planet_bp.route("/<id>", methods=["GET"])
# def get_one_planet(id):

#     try:
#         planet_id = int(id)
#     except ValueError:
#         return {"message": f"invalid id: {id}"}, 400
    
#     for planet in planet_list:
#         if planet.id == planet_id:
#             return jsonify({
#             "id": planet.id,
#             "name": planet.name,
#             "description": planet.description,
#             "position": planet.position,
#         }), 200
#     return {"message": f"id {planet_id} not found"}, 404
