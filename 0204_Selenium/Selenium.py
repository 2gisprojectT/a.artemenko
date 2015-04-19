__author__ = 'andrejartemenko'

from unittest import TestCase
import unittest
from selenium import webdriver

class Selenium(TestCase):

    def test_search(self):
        driver = webdriver.Firefox()
        driver.implicitly_wait(5)
        driver.get("http://www.apple.com/ru/")
        self.assertTrue("Apple" in driver.title, "Заголовок не соответствует ожидаемому (ожидаемый – Apple)")

        elem = driver.find_element_by_id("gh-search-submit")
        elem.click()
        elem2 = driver.find_element_by_id("gh-search-input")
        elem2.send_keys("macbook air")

        try:
            self.assertTrue("MacBook Air" in driver.page_source, "Не найдена ожидаемая строка")
        finally:
            driver.close()


    def test_search_2(self):
        driver = webdriver.Firefox()
        driver.implicitly_wait(5)
        driver.get("http://www.apple.com/ru/")
        self.assertTrue("Apple" in driver.title, "Заголовок не соответствует ожидаемому (ожидаемый – Apple)")

        elem = driver.find_element_by_id("gh-search-submit")
        elem.click()
        elem = driver.find_element_by_id("gh-search-input")
        elem.send_keys("ьфсищщл фшк")
        elem = driver.find_element_by_id("gh-search-reset")
        elem.click()
        elem = driver.find_element_by_id("gh-search-input")
        elem.send_keys("ьфсищщл фшк")

        try:
            self.assertTrue("MacBook Air" in driver.page_source, "Не найдена ожидаемая строка")
        finally:
            driver.close()


if __name__ == '__main__':
    unittest.main()