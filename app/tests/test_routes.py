import pytest

def test_get_one_planet(client, two_planets): 
    response = client.get("/planet/1")
    
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Mars",
        "description": "red rocky planet",
        "position": 4
    }
# why is this not in a list? 

def test_get_all_planet(client, two_planets):
    response = client.get("/planet")

    response_body = response.get_json() 

    assert response.status_code == 200
    assert response_body == [{
        "id": 1,
        "name": "Mars",
        "description": "red rocky planet",
        "position": 4
    }, 
    {
        "id": 2,
        "name": "Earth",
        "description": "blue marble",
        "position": 3
    }]

def test_get_nonexistent_planet(client, two_planets): 
    response = client.get("/planet/3")
    
    response_body = response.get_json()

    assert response.status_code == 404


def test_create_one_planet(client): 
    response = client.post("/planet", json={"name": "Venus",
        "description": "love planet",
        "position": 2})
    
    response_body = response.get_json()

    assert response.status_code == 201
    assert response_body["id"] == 1