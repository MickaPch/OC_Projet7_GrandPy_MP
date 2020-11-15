"""WikiMedia requests"""
from flask_grandpy.api.request import json_request




class Wiki():
    """
    Search Wikipedia page on wikimedia API.
    """

    def __init__(self, map_object):
        """Wiki object initialization"""

        self.url = "https://fr.wikipedia.org/w/api.php"

        # Wiki text for most relevant result
        self.wiki_text = self.format_wiki(map_object)

        # Info window for each marker
        info_window = {}
        for location in map_object.locations:
            info_window[location['name']] = self.format_info(
                location['name'],
                location['link']
            )

        self.info_window = info_window


    def search_pages(self, search):
        """Search information get by Google Maps API in title of wiki page"""

        params = {
            "action": "query",
            "format": "json",
            "list": "search",
            "srsearch": search,
            "srlimit": "1"
        }
        data = json_request(self.url, params)
        result = data['query']['search']

        if len(result) > 0:
            title = result[0]['title']
        else:
            raise ValueError("Aucun résultat")

        return title

    def format_description(self, search):
        """Return HTML formatted string"""

        title = self.search_pages(search)
        desc_text = self.get_desc(title)

        description = """
            <dt>{}</dt>
            <dd>{}<br>
                <a href='{}'>[En savoir plus sur wikipédia]</a>
            </dd>
        """.format(
            search,
            desc_text,
            self.get_url(title)
        )

        return description

    def get_desc(self, title):
        """"
        Search page with Wikipedia title page
        Extract of tiny description (3 sentences).
        """

        params = {
            "action": "query",
            "prop": "extracts",
            "exsentences": "3",
            "exlimit": "1",
            "titles": title,
            "explaintext": "1",
            "formatversion": "2",
            "format": "json"
        }

        data = json_request(self.url, params)
        result = data['query']['pages']

        description = result[0]['extract'].split('==')[0]

        return description

    def get_url(self, title):
        """"
        Search page with Wikipedia title page
        Get full URL of this page.
        """

        params = {
            "action": "query",
            "prop": "info",
            "titles": title,
            "inprop": "url",
            "formatversion": "2",
            "format": "json"
        }

        data = json_request(self.url, params)
        result = data['query']['pages']

        url = result[0]['fullurl']

        return url

    def format_info(self, name, link):
        """Return formatted info string to show in Maps window"""

        try:
            desc = self.get_desc(
                self.search_pages(name)
            )
        except ValueError:
            desc = """
                Je ne me souviens de rien à propos de {search}...
            """.format(search=name)

        info_window = """
        <div id="content" style="color: black;">
            <div id="siteNotice"></div>
            <h1 id="firstHeading" class="firstHeading">{title}</h1>
            <div id="bodyContent">
                <p>{desc}</p>
                <p>
                    <a href="{link}"
                       target="_blank"
                    >
                        Voir sur Google Maps
                    </a>
                </p>
            </div>
        </div>
        """.format(
            title=name,
            desc=desc,
            link=link
        )

        return info_window

    def format_wiki(self, map_object):
        """
        Return wiki text formatted
        if wiki adress description
        is the same as wiki city description
        """

        wiki_description = {
            'name': "",
            'street': "",
            'city': ""
        }
        for search in wiki_description:
            if map_object.infos[search] != "":
                try:
                    wiki_description[search] = self.format_description(
                        map_object.infos[search]
                    )
                except ValueError:
                    wiki_description[search] = """
                        <dt>{search}</dt>
                        <dd>Je ne me souviens de rien à propos de {search}...</dd>
                    """.format(search=map_object.infos[search])
            else:
                wiki_description[search] = ""

        name_desc = wiki_description['name'].split('</dt>')[1]
        try:
            address_desc = wiki_description['street'].split('</dt>')[1]
        except IndexError:
            address_desc = ""
        city_desc = wiki_description['city'].split('</dt>')[1]

        description = wiki_description['name']

        if address_desc not in (
            "",
            name_desc,
            city_desc
        ):
            description += wiki_description['street']

        if city_desc not in ("", name_desc):
            description += wiki_description['city']

        return description
