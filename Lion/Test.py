__author__ = 'andrejartemenko'

from unittest import TestCase
from Lion import Lion

import unittest


class Lion_test(TestCase):
    def setUp(self):
        self.L = Lion({('антилопа', 0): ('Лев съедает антилопу', 1)})

    def test_init(self):
        self.assertEqual(self.L.reactions, {('антилопа', 0): ('Лев съедает антилопу', 1)}, 'Инициализация работает некорректно')

    def test_get(self):
        self.L.set_state(1)
        self.assertEqual(self.L.get_state(), 1, 'Метод get_state работает не корректно')

    def test_set(self):
        self.L.set_state(0)
        self.assertEqual(self.L.state, 0, 'Метод set_state работает не корректно')


if __name__ == '__main__':
    unittest.main()
    Lion_test.init_test()