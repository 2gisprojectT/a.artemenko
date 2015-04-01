__author__ = 'andrejartemenko'

from unittest import TestCase
from Lion import Lion
from Lion import Info
from Lion import Action
import unittest


class Lion_test(TestCase):

    def test_init(self):
        L = Lion()
        self.assertTrue(L.hungry, 'Initial state is wrong')

    def test_get(self):
        L = Lion()
        self.assertTrue(L.get_state(), 'Initial state is wrong')

    def test_change(self):
        L = Lion()
        L.change_state()
        self.assertFalse(L.hungry, 'Initial state is wrong')


class Info_test(TestCase):

    def test_relations_hungry(self):
        I = Info()
        self.assertIn('Антилопа', I.relations_hungry, 'There is no Антилопа in relations_hungry')
        self.assertIn('Дерево', I.relations_hungry, 'There is no Дерево in relations_hungry')
        self.assertIn('Охотник', I.relations_hungry, 'There is no Охотник in relations_hungry')

    def test_relations_not_hungry(self):
        I = Info()
        self.assertIn('Антилопа', I.relations_not_hungry, 'There is no Антилопа in relations_not_hungry')
        self.assertIn('Дерево', I.relations_not_hungry, 'There is no Дерево in relations_not_hungry')
        self.assertIn('Охотник', I.relations_not_hungry, 'There is no Охотник in relations_not_hungry')

    def test_reaction_hungry(self):
        I = Info()
        self.assertIn('Антилопа', I.reaction_hungry, 'There is no Антилопа in reaction_hungry')
        self.assertIn('Дерево', I.reaction_hungry, 'There is no Дерево in reaction_hungry')
        self.assertIn('Охотник', I.reaction_hungry, 'There is no Охотник in reaction_hungry')

    def test_reaction_not_hungry(self):
        I = Info()
        self.assertIn('Антилопа', I.reaction_not_hungry, 'There is no Антилопа in reaction_not_hungry')
        self.assertIn('Дерево', I.reaction_not_hungry, 'There is no Дерево in reaction_not_hungry')
        self.assertIn('Охотник', I.reaction_not_hungry, 'There is no Охотник in reaction_not_hungry')


if __name__ == '__main__':
    unittest.main()
    Lion_test.init_test()
