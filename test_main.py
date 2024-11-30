import pytest
from main import app  # Import the Flask application


@pytest.fixture
def test_client():
    """Provides a test client for the Flask app."""
    app.config["TESTING"] = True  # Configure app for testing
    with app.test_client() as testing_client:
        yield testing_client  # Yield the client for use in tests


def test_homepage_status_code(test_client):
    """Checks if the homepage returns a 200 status code."""
    response = test_client.get("/")  # Perform a GET request to the homepage
    assert response.status_code == 200, "Homepage did not return status 200"
