from nlp100.helpers import string_helper
from unittest import TestCase


class TestStringHelper(TestCase):

    def test_reverse(self):
        self.assertEqual(string_helper.reverse(''), '')

        self.assertEqual(string_helper.reverse('stressed'), 'desserts')
        self.assertEqual(string_helper.reverse('0123456789'), '9876543210')

        self.assertEqual(string_helper.reverse('かるいきびんなこねこ'), 'こねこなんびきいるか')

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

    def test_remove_punctuation(self):
        alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        number = '0123456789'
        symbol = '!"#$%&\'()-^@[;:],./=~|`{+*}<>?_'

        actual = string_helper.remove_punctuation(alphabet + symbol + number)
        self.assertEqual(actual, alphabet + number)

    def test_split_into_words(self):
        actual = string_helper.split_into_words('Meow!  I like cats. ')
        self.assertEqual(actual, ['Meow!', 'I', 'like', 'cats.'])

    def test_n_gram(self):
        text = 'にくきゅう'

        actual1 = ['に', 'く', 'き', 'ゅ', 'う']
        self.assertEqual(string_helper.n_gram(text, 1), actual1)

        actual2 = ['にく', 'くき', 'きゅ', 'ゅう']
        self.assertEqual(string_helper.n_gram(text, 2), actual2)

        actual3 = ['にくき', 'くきゅ', 'きゅう']
        self.assertEqual(string_helper.n_gram(text, 3), actual3)
