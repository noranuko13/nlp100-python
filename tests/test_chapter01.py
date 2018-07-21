from nlp100 import chapter01
from unittest import TestCase


class TestChapter01(TestCase):

    def test_q00(self):
        self.assertEqual(chapter01.q00('stressed'), 'desserts')

    def test_q01(self):
        self.assertEqual(chapter01.q01('パタトクカシーー'), 'パトカー')

    def test_q02(self):
        actual = chapter01.q02('パトカー', 'タクシー')
        self.assertEqual(actual, 'パタトクカシーー')

    def test_q03(self):
        text = 'Now I need a drink, alcoholic of course, after the heavy ' \
               'lectures involving quantum mechanics.'
        expected = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]
        self.assertEqual(chapter01.q03(text), expected)

    def test_q04(self):
        text = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. ' \
               'New Nations Might Also Sign Peace Security Clause. ' \
               'Arthur King Can.'
        numbers = [1, 5, 6, 7, 8, 9, 15, 16, 19]
        expected = {'H': 1, 'He': 2, 'Li': 3, 'Be': 4, 'B': 5, 'C': 6, 'N': 7,
                    'O': 8, 'F': 9, 'Ne': 10, 'Na': 11, 'Mi': 12, 'Al': 13,
                    'Si': 14, 'P': 15, 'S': 16, 'Cl': 17, 'Ar': 18, 'K': 19,
                    'Ca': 20}

        self.assertEqual(chapter01.q04(text, numbers), expected)
