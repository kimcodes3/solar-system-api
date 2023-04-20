from flask import Blueprint

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
