from flask import Blueprint, jsonify

planet_bp = Blueprint("planet", __name__, url_prefix="/planet")

class Planet: 

    def __init__(self, id, name, description, position): 
        self.id = id
        self.name = name
        self.description = description 
        self.position = position 

earth = Planet(6, "earth", "only planet known with liquid water", 3)
mars = Planet(67, "mars", "dusty cold desert world", 4)
venus = Planet(89, "venus", "hot girl planet", 2)

planet_list = [earth, mars, venus]

@planet_bp.route("", methods=["GET"])
def get_planets():
    response = []
    for planet in planet_list:
        planet_dict = {
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "position": planet.position,
        }
        response.append(planet_dict)
    return jsonify(response), 200

@planet_bp.route("/<id>", methods=["GET"])
def get_one_planet(id):

    try:
        planet_id = int(id)
    except ValueError:
        return {"message": f"invalid id: {id}"}, 400
    
    for planet in planet_list:
        if planet.id == planet_id:
            return jsonify({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "position": planet.position,
        }), 200
    return {"message": f"id {planet_id} not found"}, 404
