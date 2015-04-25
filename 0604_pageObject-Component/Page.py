__author__ = 'andrejartemenko'

from search_bar import SearchBar

class Page():
    def __init__(self, driver):
        self.Driver = driver
        self._search_bar = None

    @property
    def search_bar(self):
        if self._search_bar is None:
            self._search_bar = \
                SearchBar(self.Driver)
        return self._search_bar

    def open(self, url):
        self.Driver.get(url)

    @property
    def title(self):
        return self.Driver.title