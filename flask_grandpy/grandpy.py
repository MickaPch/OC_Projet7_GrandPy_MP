import functools
from string import digits

from flask import (
    Blueprint,
    flash,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for,
    Response,
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
        grandpy_adresse = ''
        grandpy_map = ''
        wiki_name = ''
        grandpy_suite = ''
        positions = []

        if message in [None, '']:
            error = "Parles un peu plus fort mon petit !"
        
        # Parsing
        lieu = parse_string(message)
        wiki_name = ""
        wiki_adress = ""

        if lieu in [None, '']:
            error = """Je suis désolé mon enfant, mais je n'ai pas bien compris ce que tu recherches.<br>
Pourrais-tu être un peu plus précis ?"""
        else:
            maps = Gmaps(lieu)
            positions = []

            if maps.nb_places > 1:
                grandpy_adresse = "Alors, d'après mes souvenirs, plusieurs lieux correspondaient à ce lieu :<br><ul>"
                for place in maps.locations:
                    grandpy_adresse += "<li>{} : {}</li>".format(
                        place['name'],
                        place['address']
                    )
                    grandpy_map = "Les voici sur une carte :"

                    wiki_name = search_wiki(name=place['name'])
                    wiki_adress = search_wiki(adress=place['formatted_address'].split(',')[0].maketrans('', '', digits))



                    # Marqueurs
                    positions.append({
                        'lat': lieu['geometry']['location']['lat'],
                        'lng': lieu['geometry']['location']['lng'],
                        'name': lieu['name'],
                        'wiki_name': wiki_name,
                        'wiki_adress': wiki_adress
                    })
                    # print(wiki_name)
                grandpy_adresse += "</ul>"




            elif maps.nb_places == 1:
                grandpy_adresse = "Tu veux l'adresse de {} ?<br>Bien sûr ! La voici : {}".format(
                    maps.name,
                    maps.address
                )
                grandpy_map = "C'est ici :"

                # Marqueur
                wiki_name = Wiki(
                    maps.name,
                    maps.link
                )
                wiki_street = Wiki(maps.street)
                wiki_ville = Wiki(maps.city)


                wiki_title = "{} - {} :".format(
                    maps.name,
                    maps.address
                )
                wiki_text = wiki_name.description
                address_desc = wiki_street.description.split('</dt>')[1]
                ville_desc = wiki_ville.description.split('</dt>')[1]
                if address_desc != ville_desc:
                    wiki_text += wiki_street.description
                wiki_text += wiki_ville.description

                positions.append({
                    'lat': maps.lat,
                    'lng': maps.lng,
                    'name': maps.name,
                    # 'wiki_name': wiki_name.desc_text,
                    'content': wiki_name.info_window
                })
            else:
                error = """Je pense que ma mémoire commence à me jouer des tours...<br>
Je ne me souviens de rien à propos de {}""".format(lieu)


        grandpy_suite = "Alors, content ? Veux-tu que je te parles d'un autre lieu ?"

        data = {
            'error': error,
            'message': message,
            'grandpy_adresse': grandpy_adresse,
            'grandpy_map': grandpy_map,
            'wiki_title': wiki_title,
            'grandpy_wiki': wiki_text,
            'grandpy_suite': grandpy_suite,
            'location': positions,
            'link_js': MAPS_LINK
        }
        # print(data)
    
    # import time
    # time.sleep(3)

    return jsonify(data)