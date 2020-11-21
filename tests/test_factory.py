"""Test Home page"""
from flaskgrandpy import create_app


def test_config():
    """Test environment"""
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing

def test_home(client):
    """Test home page"""
    response = client.get('/')
    assert b'GrandPy Bot' in response.data
