"""Word parser"""
import json
import os
import string


def load_words(filename):
    """Return stopwords list from JSON"""
    path_file = os.path.join(os.path.dirname(__file__), filename)
    with open(path_file, 'rb') as jsonf:
        stopwords = json.load(jsonf)

    return stopwords

def parse_string(pstring):
    """Return pstring parsed without stopwords"""

    stopwords = list(
        set(load_words('stopwords.json')) | set(load_words('add_words.json'))
    )

    split_string = pstring.lower().replace(
        "'",
        " "
    ).replace(
        "-",
        " "
    ).translate(
        str.maketrans(
            '',
            '',
            string.punctuation
        )
    ).split()

    pstring = " ".join(
        set(split_string) - set(stopwords)
    )

    return pstring
