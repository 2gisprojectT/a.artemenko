__author__ = 'andrejartemenko'

from unittest import TestCase
from Lion import Lion

import unittest


class Lion_test(TestCase):
    def setUp(self):
        self.test_dict = {('антилопа', 'голодный'): ('Лев съедает антилопу', 'сытый')}
        self.test_object = 'антилопа'
        self.test_state = 'голодный'
        self.L = Lion(self.test_dict, self.test_state)

    def test_init(self):
        self.assertEqual(self.L.reactions, self.test_dict, 'Инициализация работает некорректно (словарь)')
        self.assertEqual(self.L.state, self.test_state, 'Инициализация работает некорректно (состояние Льва)')


    def test_decide(self):
        self.decide_result = self.L.decide(self.test_object)
        self.assertEqual(self.decide_result, self.test_dict[self.test_object, self.test_state][0], 'Метод decide возвращает неверное значение')
        self.assertEqual(self.L.state, self.test_dict[self.test_object, self.test_state][1], 'Метод decide не изменил состояние Льва')
        self.assertEqual(self.L.action, self.test_dict[self.test_object, self.test_state][0], 'Метод decide не изменил действие Льва')

    def test_decide_negative(self):
        self.assertRaises(Exception, self.L.decide, 'какая-то строка')


if __name__ == '__main__':
    unittest.main()