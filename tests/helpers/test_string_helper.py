from nlp100.helpers import string_helper
import pytest
import re


class TestStringHelper:

    def test_reverse(self):
        assert string_helper.reverse('') == ''

        assert string_helper.reverse('stressed') == 'desserts'
        assert string_helper.reverse('0123456789') == '9876543210'

        assert string_helper.reverse('かるいきびんなこねこ') == 'こねこなんびきいるか'

    def test_odd(self):
        assert string_helper.odd('パタトクカシーー') == 'パトカー'
        assert string_helper.odd('プチリョンコ') == 'プリン'

    def test_even(self):
        assert string_helper.even('パタトクカシーー') == 'タクシー'
        assert string_helper.even('プチリョンコ') == 'チョコ'

    def test_alternate(self):
        with pytest.raises(ValueError):
            string_helper.alternate('はみがき', 'むしば')

        actual = string_helper.alternate('プリン', 'チョコ')
        assert actual == 'プチリョンコ'

    def test_remove_punctuation(self):
        alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        number = '0123456789'
        symbol = '!"#$%&\'()-^@[;:],./=~|`{+*}<>?_'

        actual = string_helper.remove_punctuation(alphabet + symbol + number)
        assert actual == alphabet + number

    def test_split_into_words(self):
        actual = string_helper.split_into_words('Meow!  I like cats. ')
        assert actual == ['Meow!', 'I', 'like', 'cats.']

    def test_n_gram(self):
        text = 'にくきゅう'

        actual1 = ['に', 'く', 'き', 'ゅ', 'う']
        assert string_helper.n_gram(text, 1) == actual1

        actual2 = ['にく', 'くき', 'きゅ', 'ゅう']
        assert string_helper.n_gram(text, 2) == actual2

        actual3 = ['にくき', 'くきゅ', 'きゅう']
        assert string_helper.n_gram(text, 3) == actual3

    def test_cipher(self):
        assert string_helper.cipher('abcdefghijklmnopqrstuvwxyz') == 'zyxwvutsrqponmlkjihgfedcba'
        assert string_helper.cipher('ABCDEFGHIJKLMNOPQRSTUVWXYZ') == 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        number = '0123456789'
        assert string_helper.cipher(number) == number

        symbol = '!"#$%&\'()-^@[;:],./=~|`{+*}<>?_'
        assert string_helper.cipher(symbol) == symbol

    def test_typoglycemia(self):
        assert string_helper.typoglycemia('') == ''
        assert string_helper.typoglycemia('1 12 123 1234') == '1 12 123 1234'

        actual = string_helper.typoglycemia('12345')
        assert re.match(r'1(234|243|324|342|423|432)5', actual)
