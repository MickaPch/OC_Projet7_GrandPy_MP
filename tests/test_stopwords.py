"""Test STOPWORDS module"""
from flaskgrandpy.parser import stopwords


def test_stopwords():
    """Test load json file"""
    list_words = stopwords.load_words('stopwords.json')

    assert 'absolument' in list_words

def test_parse():
    """Test parse string"""
    pstring = "Bonjour le absolument OpenClassrooms PARIS"

    pstring = stopwords.parse_string(pstring)

    assert 'paris' in pstring
    assert 'openclassrooms' in pstring
    assert 'bonjour' not in pstring
    assert 'absolument' not in pstring
