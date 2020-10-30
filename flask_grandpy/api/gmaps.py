# Clé API : AIzaSyBD0DjPZQJNI-2XLgRE_TB5Y6-TJT88atg
# Nom du projet : GrandPy-OC
# ID projet Google Maps : alert-almanac-292209
# N° du projet : 1027604431478

import requests
from string import digits

from flask_grandpy.settings import API_KEY


MAPS_LINK = "https://maps.googleapis.com/maps/api/js?key={}&libraries=localContext,places&callback=initMap".format(
    API_KEY
)

# Créer CLASSE + Vérification nombre de résultats pour choix utilisateur
class Gmaps():

    def __init__(self, place):

        self._url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"
        link_url = "https://www.google.com/maps/search/?api=1&query={}&query_place_id={}"

        request = self.request_get(place)
        self.nb_places = len(request['candidates'])

        if self.nb_places > 0:
                
            # Relevant place:
            self.name = request['candidates'][0]['name']
            self.address = request['candidates'][0]['formatted_address']
            self.street = self.address.split(',')[-3].translate(
                str.maketrans('', '', digits)
            ).strip()
            self.city = self.address.split(',')[-2].translate(
                str.maketrans('', '', digits)
            ).strip()
            self.lat = request['candidates'][0]['geometry']['location']['lat']
            self.lng = request['candidates'][0]['geometry']['location']['lng']
            self.link = link_url.format(
                requests.utils.requote_uri(self.address),
                request['candidates'][0]['place_id']
            )

            # All places, usefull if nb_places > 1
            self.locations = []
            for match_place in request['candidates']:
                address = match_place['formatted_address']
                street = address.split(',')[-3].translate(
                    str.maketrans('', '', digits)
                ).strip()
                city = address.split(',')[-2].translate(
                    str.maketrans('', '', digits)
                ).strip()
                link = link_url.format(
                    requests.utils.requote_uri(address),
                    match_place['place_id']
                )

                self.locations.append({
                    'name': match_place['name'],
                    'address': address,
                    'street': street,
                    'city': city,
                    'link': link
                })

    def request_get(self, place):

        params = {
            "input": place,
            "inputtype": "textquery",
            "fields": "formatted_address,name,geometry,place_id",
            # "fields": ["formatted_address", "name", "geometry", "place_id"],
            "key": API_KEY
        }

        S = requests.Session()
        R = S.get(url=self._url, params=params)

        return R.json()


def request_map_api(lieu):
    # map_request_url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={}&inputtype=textquery&fields=formatted_address,name,geometry,icon&key={}".format(
    #     lieu,
    #     API_KEY
    # )
    # map_request_url = requests.utils.requote_uri(map_request_url)
    # resp = requests.get(map_request_url)
    # map_api = resp.json()

    return map_api
