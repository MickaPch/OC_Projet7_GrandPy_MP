"""Tests configuration"""
# pylint: disable=redefined-outer-name
# ^^^ this
import pytest

from flaskgrandpy import create_app

@pytest.fixture
def app():
    """Configure the app for testing"""
    app = create_app({
        'TESTING': True
    })

    yield app

@pytest.fixture
def client(app):
    """Test access the root off the application"""
    return app.test_client()

@pytest.fixture
def runner(app):
    """Test running app"""
    return app.test_cli_runner()
