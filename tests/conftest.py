import pytest
from icav_tech_challenge.app import create_app





@pytest.fixture(scope='module')
def test_client():
    # Create a Flask app configured for testing
    flask_app=create_app()
    
    flask_app.config["TESTING"] = True
    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as testing_client:
        # Establish an application context
        with flask_app.app_context():
            yield testing_client 


