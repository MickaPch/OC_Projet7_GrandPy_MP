import json
import os
import string


def load_words(filename):
    """Return stopwords list from JSON"""
    path_file = os.path.join(os.path.dirname(__file__), filename)
    with open(path_file, 'rb') as f:
        stopwords = json.load(f)

    return stopwords

def parse_string(s):
    """Return s parsed without stopwords"""

    stopwords = list(
        set(load_words('stopwords.json')) | set(load_words('add_words.json'))
    )

    split_string = s.lower().replace(
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

    s = " ".join(
        set(split_string) - set(stopwords)
    )

    return s