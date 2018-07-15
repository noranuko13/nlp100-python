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
