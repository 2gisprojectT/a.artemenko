__author__ = 'andrejartemenko'

from unittest import TestCase
import unittest
from selenium import webdriver
from Page import Page

class Selenium(TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.page = Page(self.driver)
        self.driver.implicitly_wait(10)
        self.page.open("http://www.apple.com/ru/")
        self.assertTrue("Apple" in self.page.title, "Заголовок не соответствует ожидаемому (ожидаемый – Apple)")

    def tearDown(self):
        self.driver.close()

    def test_search(self):
        self.page.search_bar.search("macbook air")
        self.assertTrue("MacBook Air" in self.driver.page_source, "Не найдена ожидаемая строка")

    def test_search_2(self):
        self.page.search_bar.search_and_reset("ьфсищщл фшк")
        self.page.search_bar.search("macbook air")
        self.assertTrue("MacBook Air" in self.driver.page_source, "Не найдена ожидаемая строка")

if __name__ == '__main__':
    unittest.main()