"""Request function for APIs"""
import requests


def json_request(url, params):
    """Return JSON request from given url and dict of params"""

    session = requests.Session()
    request = session.get(url=url, params=params)

    return request.json()
