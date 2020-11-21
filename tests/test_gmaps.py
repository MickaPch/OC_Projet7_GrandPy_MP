"""Test GMAPS module"""
from flaskgrandpy.api import gmaps


def test_gmaps_none():
    """Test none place"""
    map_test = gmaps.Gmaps('')

    assert map_test.nb_places == 0

def test_get_one_result():
    """Test unique result"""
    map_test = gmaps.Gmaps('openclassrooms')

    assert map_test.nb_places == 1
    assert map_test.infos['name'] == 'Openclassrooms'
    assert 'Charente' in map_test.infos['address']
    assert len(map_test.locations) == 1
    assert map_test.locations[0]['lat'] < 49 and map_test.locations[0]['lat'] > 48
    assert map_test.locations[0]['address'] == map_test.infos['address']

    map_test = gmaps.Gmaps('gare tournefeuille')

    assert map_test.infos['street'] == ""

def test_get_multi_results():
    """Test multi-results"""
    map_test = gmaps.Gmaps('airbus toulouse')

    assert map_test.nb_places > 1
    assert 'Airbus' in map_test.infos['name']
    assert 'Toulouse' in map_test.infos['address']
    assert len(map_test.locations) > 1
    assert map_test.locations[0]['lat'] < 44 and map_test.locations[0]['lat'] > 43
    assert map_test.locations[0]['address'] == map_test.infos['address']
