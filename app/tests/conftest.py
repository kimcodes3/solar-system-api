from app import create_app, db
import pytest
from app.models.planet import Planet
from flask.signals import request_finished

@pytest.fixture
def app(): 
    app = create_app(test_config=True)

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra): 
        db.session.remove()

    with app.app_context(): 
        db.create_all()
        yield app 
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def two_planets(): 
    mars = Planet(name="Mars", description="red rocky planet", position=4)
    earth = Planet(name="Earth", description="blue marble", position=3)

    db.session.add_all([mars, earth])
    db.session.commit()