"""Google Maps requests"""
from string import digits
import requests

from flaskgrandpy.api.request import json_request, retrieve_api_key


google_map_key = retrieve_api_key('./config.yaml')
MAPS_LINK = "https://maps.googleapis.com/maps/api/js?" \
            "key={}&libraries=localContext,places&callback=initMap".format(
                google_map_key
            )

class Gmaps():
    """
    Search of location by text.
    Return nb of found places.
    """


    def __init__(self, place, request=None):
        """
        Object search place init.
        Return nb of found places.
        """
        self.url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
        self.link_url = "https://www.google.com/maps/search/?api=1&query={}&query_place_id={}"

        # API REQUEST
        if request is None:
            request = self.get_request(place)

        # NB of found places
        self.nb_places = len(request['results'])

        if self.nb_places > 0:

            # Most relevant place if nb_places > 1
            self.infos = self.get_infos(request)

            # All results in list for Javascript Map
            self.locations = self.get_locations(request)

            str_address, str_wiki = self.cards_text()
            if self.nb_places == 1:
                self.messages = {
                    'card_map': "C'est ici :",
                    'card_address': str_address,
                    'card_wiki': str_wiki
                }
            else:
                self.messages = {
                    'card_map': "Les voici sur une carte :",
                    'card_address': str_address,
                    'card_wiki': str_wiki
                }

    def get_request(self, place):
        """Return Gmaps request JSON object"""
        params = {
            "query": place,
            "key": google_map_key
        }

        return json_request(self.url, params)

    def get_infos(self, request):
        """Return infos dict"""

        name = request['results'][0]['name']
        address = request['results'][0]['formatted_address']
        try:
            street = address.split(',')[-3].translate(
                str.maketrans('', '', digits)
            ).strip()
        except IndexError:
            street = ""
        city = address.split(',')[-2].translate(
            str.maketrans('', '', digits)
        ).strip()

        # URL Google maps

        link = self.link_url.format(
            requests.utils.requote_uri(address),
            request['results'][0]['place_id']
        )
        return {
            'name': name,
            'address': address,
            'street': street,
            'city': city,
            'link': link
        }

    def get_locations(self, request):
        """Return list of locations informations"""
        locations = []
        for match_place in request['results'][:5]:

            locations.append({
                'lat': match_place['geometry']['location']['lat'],
                'lng': match_place['geometry']['location']['lng'],
                'name': match_place['name'],
                'address': match_place['formatted_address'],
                'link': self.link_url.format(
                    requests.utils.requote_uri(
                        match_place['formatted_address']
                    ),
                    match_place['place_id']
                )
            })

        return locations

    def cards_text(self):
        """Return formatted string for adress and wiki cards"""

        if self.nb_places == 1:
            str_address = "Tu veux l'adresse de {} ?<br>Bien sûr ! La voici : {}".format(
                self.infos['name'],
                self.infos['address']
            )
            str_wiki = "{} - {} :".format(
                self.infos['name'],
                self.infos['address']
            )
        else:
            # PLUSIEURS RESULTATS
            list_content = str()
            for location in self.locations:
                list_content += "<li>{} : {}</li>".format(
                    location['name'],
                    location['address']
                )
            str_address = "Alors, d'après mes souvenirs, plusieurs endroits " \
                        "correspondaient à ce lieu :<br><ul>{}</ul>".format(
                            list_content
                        )
            str_wiki = "Plusieurs endroits correspondent à ce lieu." \
                    " Voici celui que j'estime le plus pertinent :<br>{} - {}".format(
                        self.infos['name'],
                        self.infos['address']
                    )

        return str_address, str_wiki
