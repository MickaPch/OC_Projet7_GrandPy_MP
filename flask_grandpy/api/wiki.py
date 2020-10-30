import requests


class Wiki():

    def __init__(self, search=None, link=None):

        self._url = "https://fr.wikipedia.org/w/api.php"

        self.match = False
        self.info_window = ""
        if search != None:
            try:
                title = self.search_pages(search)
                self.description = self.format_description(search, title)
                self.match = True
            except ValueError:
                self._desc_text = 'Je ne me souviens de rien à propos de ce lieu...'
                self.description = """
                    <dt>{search}</dt>
                    <dd>Je ne me souviens de rien à propos de {search}...</dd>
                """.format(search=search)
            if link != None:
                self.info_window = self.format_info(
                    search,
                    link
                )

    def wiki_request(self, params):

        S = requests.Session()
        R = S.get(url=self._url, params=params)

        return R.json()

    def search_pages(self, search):
        """Search information get by Google Maps API in title of wiki page"""

        params = {
            "action": "query",
            "format": "json",
            "list": "search",
            "srsearch": search,
            "srlimit": "1"
        }
        DATA = self.wiki_request(params)
        result = DATA['query']['search']

        if len(result) > 0:
            title = result[0]['title']
        else:
            raise ValueError("Aucun résultat")

        return title

    def format_description(self, search, title):
        """Return HTML formatted string"""

        self._desc_text = self.get_desc(title)

        description = """
            <dt>{}</dt>
            <dd>{}<br>
                <a href='{}'>[En savoir plus sur wikipédia]</a>
            </dd>
        """.format(
            search,
            self._desc_text,
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

        DATA = self.wiki_request(params)
        result = DATA['query']['pages']

        if len(result) > 0:
            description = result[0]['extract'].split('==')[0]
        else:
            raise ValueError("Aucun résultat")

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

        DATA = self.wiki_request(params)
        result = DATA['query']['pages']

        if len(result) > 0:
            url = result[0]['fullurl']
        else:
            raise ValueError("Aucun résultat")

        return url

    def format_info(self, search, link):
        """Return formatted info string to show in Maps window"""

        info_window = """
        <div id="content">
            <div id="siteNotice"></div>
            <h1 id="firstHeading" class="firstHeading">{title}</h1>
            <div id="bodyContent">
                <p>{desc}</p>
                <p><a href="{link}" target="_blank">Voir sur Google Maps</a></p>
            </div>
        </div>
        """.format(
            title=search,
            desc=self._desc_text,
            link=link
        )


        return info_window