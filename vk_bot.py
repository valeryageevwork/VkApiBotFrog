import os
import requests

from forismatic import forismatic
from pyunsplash import PyUnsplash


class VkBot:
    def __init__(self):
        self._COMMANDS = ['/помощь', "/ква-котик", "/ква-мотивация", '/фотожаба']
        self.api_key_splash = os.getenv("SPLASH_API_ID")
        self.api_key_cats = os.getenv("CATS_API_ID")

    def new_message(self, message):
        if message == self._COMMANDS[0]:
            str_commands = ('Квак-команды:\n\n' +
                            '/фотожаба - жабка\n' +
                            '/ква-котик - милый котик\n' +
                            '/ква-мотивация - цитата великих людей\n')
            return str_commands
        elif message == self._COMMANDS[1]:
            return self.cats()
        elif message == self._COMMANDS[2]:
            return self.quote()
        elif message == self._COMMANDS[3]:
            return self.frogs()

    def cats(self):
        r = requests.get('https://api.thecatapi.com/v1/images/search?api_key=' + self.api_key_cats).json()
        return r[0]["url"]

    def frogs(self):
        pu = PyUnsplash(api_key=self.api_key_splash)
        photos = pu.photos(type_='random', count=1, featured=True, query="frogs")
        [photo] = photos.entries

        return photo.link_download

    def quote(self):
        f = forismatic.ForismaticPy()
        q = f.get_Quote(language='ru')
        str = q[0] + '\n\n' + q[1]
        return str


