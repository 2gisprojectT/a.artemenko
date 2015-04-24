__author__ = 'andrejartemenko'


class BaseComponent(object):
    def __init__(self, driver, element=None):
        self.driver = driver
        self.element = element