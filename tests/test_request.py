"""Test REQUEST module"""
from flaskgrandpy.api import request


def test_request():
    """Test known request to wikipedia API"""

    json_req = request.json_request(
        "https://fr.wikipedia.org/w/api.php",
        {
            "action": "query",
            "format": "json",
            "list": "search",
            "srsearch": "kjbfiurgifr",
            "srlimit": "1"
        }
    )

    assert 'query' in json_req
