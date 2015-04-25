__author__ = 'andrejartemenko'

from base_component import BaseComponent


class SearchBar(BaseComponent):
    selectors = {
        'submit': 'gh-search-submit',
        'input': 'gh-search-input',
        'reset': 'gh-search-reset'
    }

    def search(self, query):
        self.driver.find_element_by_id(self.selectors['submit']).click()
        self.driver.find_element_by_id(self.selectors['input']).send_keys(query)
        self.driver.find_element_by_id(self.selectors['submit']).click()

    def search_and_reset(self, query):
        self.driver.find_element_by_id(self.selectors['submit']).click()
        self.driver.find_element_by_id(self.selectors['input']).send_keys(query)
        self.driver.find_element_by_id(self.selectors['reset']).click()