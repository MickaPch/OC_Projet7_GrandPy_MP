"""Test WIKIMEDIA module"""
from flaskgrandpy.api import gmaps
from flaskgrandpy.api import wiki


def test_wiki():
    """Test known result"""
    gmaps_test = gmaps.Gmaps('openclassrooms')
    wiki_test = wiki.Wiki(gmaps_test)

    assert "cours" in wiki_test.wiki_text

def test_wrong_wiki():
    """Test known none result"""
    gmaps_test = gmaps.Gmaps('Airbus M67')
    wiki_test = wiki.Wiki(gmaps_test)

    assert "Je ne me souviens de rien" in wiki_test.wiki_text

def test_wrong_adress():
    """Test known wrong address"""
    gmaps_test = gmaps.Gmaps('gare tournefeuille')
    wiki_test = wiki.Wiki(gmaps_test)

    assert "Tournefeuille" in wiki_test.wiki_text
