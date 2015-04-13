__author__ = 'andrejartemenko'

from unittest import TestCase
from Lion import Lion

import unittest


class Lion_test(TestCase):
    def setUp(self):
        self.L = Lion({('антилопа', 'голодный'): ('Лев съедает антилопу', 'сытый')}, 'голодный')

    def test_init(self):
        self.assertEqual(self.L.reactions, {('антилопа', 'голодный'): ('Лев съедает антилопу', 'сытый')}, 'Инициализация работает некорректно (словарь)')
        self.assertEqual(self.L.state, 'голодный', 'Инициализация работает некорректно (состояние Льва)')

    def test_decide(self):
        self.assertEqual(self.L.decide('антилопа'), 'Лев съедает антилопу', 'Метод decide возвращает неверное значение')
        self.assertEqual(self.L.state, 'сытый', 'Метод decide не изменил состояние Льва')
        self.assertEqual(self.L.action, 'Лев съедает антилопу', 'Метод decide не изменил действие Льва')


if __name__ == '__main__':
    unittest.main()
    Lion_test.init_test()