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
        text = 'Now I need a drink, alcoholic of course, ' \
               'after the heavy lectures involving quantum mechanics.'
        expected = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]
        self.assertEqual(chapter01.q03(text), expected)

    def test_q04(self):
        text = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also ' \
               'Sign Peace Security Clause. Arthur King Can.'
        numbers = [1, 5, 6, 7, 8, 9, 15, 16, 19]
        expected = {'H': 1, 'He': 2, 'Li': 3, 'Be': 4, 'B': 5, 'C': 6, 'N': 7, 'O': 8, 'F': 9,
                    'Ne': 10, 'Na': 11, 'Mi': 12, 'Al': 13, 'Si': 14, 'P': 15, 'S': 16, 'Cl': 17,
                    'Ar': 18, 'K': 19, 'Ca': 20}

        self.assertEqual(chapter01.q04(text, numbers), expected)

    def test_q05(self):
        text = 'I am an NLPer'

        expected_words = [['I', 'am'], ['am', 'an'], ['an', 'NLPer']]
        self.assertEqual(chapter01.q05_word(text), expected_words)

        expected_chars = ['I ', ' a', 'am', 'm ', ' a', 'an', 'n ', ' N', 'NL', 'LP', 'Pe', 'er']
        self.assertEqual(chapter01.q05_char(text), expected_chars)

    def test_q06(self):
        # x = {'ap', 'ar', 'pa', 'ra', 'di', 'is', 'ad', 'se'}
        # y = {'ap', 'ar', 'pa', 'ra', 'ag', 'ph', 'gr'}
        x = set(chapter01.q05_char('paraparaparadise'))
        y = set(chapter01.q05_char('paragraph'))

        expected_union = {'ap', 'ar', 'pa', 'ra',
                          'di', 'is', 'ad', 'se', 'ag', 'ph', 'gr'}
        self.assertEqual(chapter01.q06_union(x, y), expected_union)

        expected_intersection = {'ap', 'ar', 'pa', 'ra'}
        self.assertEqual(chapter01.q06_intersection(x, y), expected_intersection)

        expected_symmetric_differences = {'di', 'is', 'ad', 'se', 'ag', 'ph', 'gr'}
        self.assertEqual(chapter01.q06_symmetric_difference(x, y), expected_symmetric_differences)

        z = {'se'}
        self.assertTrue(z.issubset(x))
        self.assertFalse(z.issubset(y))

    def test_q07(self):
        self.assertEqual(chapter01.q07_template('x', 'y', 'z'), 'x時のyはz')
        self.assertEqual(chapter01.q07_template(12, '気温', 22.4), '12時の気温は22.4')
        self.assertEqual(chapter01.q07_template(3, 'おやつ', '金米糖'), '3時のおやつは金米糖')

    def test_q08(self):
        plain = 'Hi He Lied Because Boron Could Not Oxidize Fluorine.'
        expected = 'Hr Hv Lrvw Bvxzfhv Blilm Clfow Nlg Ocrwrav Foflirmv.'

        ciphertext = chapter01.q08(plain)
        self.assertEqual(ciphertext, expected)

        self.assertEqual(chapter01.q08(ciphertext), plain)
