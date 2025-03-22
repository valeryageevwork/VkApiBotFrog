import json
import os
import pinterest
import requests
from forismatic import forismatic


class VkBot:
    def __init__(self):
        self._COMMANDS = ["/котик", "/мотивация", "/собачка", "/муркосмос", "/библейские_цитаты", "/мужское", "/женское"]
        self.api_key_cats = os.getenv("CATS_API_ID")
        self.api_key_nasa = os.getenv("NASA_API_ID")

    def new_message(self, message):
        if message == self._COMMANDS[0]:
            return self.cats()
        elif message == self._COMMANDS[1]:
            return self.quote()
        elif message == self._COMMANDS[2]:
            return self.dogs()
        elif message == self._COMMANDS[3]:
            return self.nasapic()
        elif message == self._COMMANDS[4]:
            return self.bible()

    def cats(self):
        r = requests.get('https://api.thecatapi.com/v1/images/search?api_key=' + self.api_key_cats).json()
        return r[0]["url"]

    def quote(self):
        f = forismatic.ForismaticPy()
        q = f.get_Quote(language='ru')
        str = q[0] + '\n\n' + q[1]
        return str

    def dogs(self):
        r = requests.get('https://dog.ceo/api/breeds/image/random').json()
        return r["message"]

    def nasapic(self):
        f = r"https://api.nasa.gov/planetary/apod?api_key=" + self.api_key_nasa + "&count=1"
        data = requests.get(f)
        tt = json.loads(data.text)
        return tt[0]["url"]

    def bible(self):
        f = r"https://justbible.ru/api/random?translation=rbo"
        data = requests.get(f)
        tt = data.json()
        return tt["verse"] + "\n\n" + tt["info"]

    def man(self):
        link = pinterest.oauth2.authorization_url(os.getenv("1514198"), "http://localhost:8000/callback")
        api = pinterest.Pinterest(token=os.getenv("2865a5585a2213fd9e0a73c4161b3f68a375f0d9"))
        js = api.search_pins("men's style", cursor=None)
        url js['media']['images']['original']['url']
