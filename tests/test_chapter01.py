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
