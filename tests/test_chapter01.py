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
