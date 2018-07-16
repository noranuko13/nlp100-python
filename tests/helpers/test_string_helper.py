from nlp100.helpers import string_helper
from unittest import TestCase


class TestStringHelper(TestCase):

    def test_reverse(self):
        self.assertEqual(string_helper.reverse(''), '')

        self.assertEqual(string_helper.reverse('stressed'), 'desserts')
        self.assertEqual(string_helper.reverse('0123456789'), '9876543210')

        self.assertEqual(
            string_helper.reverse('かるいきびんなこねこ'),
            'こねこなんびきいるか'
        )

    def test_odd(self):
        self.assertEqual(string_helper.odd('パタトクカシーー'), 'パトカー')
        self.assertEqual(string_helper.odd('プチリョンコ'), 'プリン')

    def test_even(self):
        self.assertEqual(string_helper.even('パタトクカシーー'), 'タクシー')
        self.assertEqual(string_helper.even('プチリョンコ'), 'チョコ')

    def test_alternate(self):
        with self.assertRaises(ValueError):
            string_helper.alternate('はみがき', 'むしば')

        actual = string_helper.alternate('プリン', 'チョコ')
        self.assertEqual(actual, 'プチリョンコ')
