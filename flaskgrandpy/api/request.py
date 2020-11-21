"""Request function for APIs"""
import requests
import yaml


def json_request(url, params):
    """Return JSON request from given url and dict of params"""

    session = requests.Session()
    request = session.get(url=url, params=params)

    return request.json()

def retrieve_api_key(file_path):
    """Retrieve GOOGLE_MAP_KEY from yaml file"""

    with open(file_path) as yamlfile:

        yaml_load = yaml.load(yamlfile, Loader=yaml.Loader)
        google_api_key = yaml_load['GOOGLE_MAP_KEY']

    return google_api_key
