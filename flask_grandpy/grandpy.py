"""GrandPy app"""
from flask import (
    Blueprint,
    render_template,
    request,
    jsonify
)

from flask_grandpy.parser.stopwords import parse_string
from flask_grandpy.api.gmaps import Gmaps, MAPS_LINK
from flask_grandpy.api.wiki import Wiki


bp = Blueprint(
    'grandpy',
    __name__
)

@bp.route('/', methods=('GET', 'POST'))
def index():
    """Routing to main page"""

    return render_template('grandpy.html')

@bp.route('/show_response', methods=('GET', 'POST'))
def show_response():
    """
    Retrieve message from user.
    Parse the message to search the location.
    Search location in Google Maps API.
    Search location in Wikipedia API.
    Return results to user.
    """
    if request.method == 'POST':
        message = request.form['message']
        error = None

        if message.strip() in [None, '']:
            error = "Parles un peu plus fort mon petit !"
            data = {
                'error': error
            }

        else:
            # Parsing user message
            search = parse_string(message)

            if search.strip() in [None, '']:
                error = "Je suis désolé mon enfant, mais je n'ai pas bien compris" \
                        " ce que tu recherches.<br>Pourrais-tu être un peu plus précis ?"
                data = {
                    'error': error
                }

            else:
                data = search_place(search, message)
    else:
        data = {'error': "Désolé, seule la méthode POST est gérée pour le traitement de l'information."}

    return jsonify(data)

def search_place(search, message):
    """
    Search a place in Google Maps API.
    If no places found, return error to show in HTML template.
    Else, return maps and wiki informations about this places."""

    error = None
    maps = Gmaps(search)

    if maps.nb_places == 0:
        error = """Je pense que ma mémoire commence à me jouer des tours...<br>
Je ne me souviens de rien à propos de {}""".format(search)
        data = {
            'error': error
        }

    else:
        # 1 ou plusieurs résultats

        # Wikimedia search by name, street and city
        wiki = Wiki(maps)

        locations = []
        for location in maps.locations:
            location['content'] = wiki.info_window[
                location['name']
            ]
            locations.append(location)

        data = {
            'error': error,
            'message': message,
            'grandpy_adresse': maps.messages['card_address'],
            'grandpy_map': maps.messages['card_map'],
            'wiki_title': maps.messages['card_wiki'],
            'grandpy_wiki': wiki.wiki_text,
            'location': locations,
            'link_js': MAPS_LINK
        }

    return data
