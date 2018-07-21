from nlp100.helpers import string_helper
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
