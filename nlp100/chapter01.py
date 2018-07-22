from nlp100.helpers import string_helper
from typing import Dict
from typing import List


def q00(word) -> str:
    return string_helper.reverse(word)


def q01(word) -> str:
    return string_helper.odd(word)


def q02(first, second) -> str:
    return string_helper.alternate(first, second)


def q03(text) -> List[int]:
    text = string_helper.remove_punctuation(text)
    words = string_helper.split_into_words(text)
    return [len(word) for word in words]


def q04(text, numbers) -> Dict[str, int]:
    chemical_symbols = {}
    text = string_helper.remove_punctuation(text)
    words = string_helper.split_into_words(text)

    for i, word in enumerate(words, start=1):
        chemical_symbols[word[0:1 if i in numbers else 2]] = i

    return chemical_symbols


def q05_word(text) -> List[List[str]]:
    words = string_helper.split_into_words(text)
    return string_helper.n_gram(words, 2)


def q05_char(text) -> List[str]:
    return string_helper.n_gram(text, 2)
