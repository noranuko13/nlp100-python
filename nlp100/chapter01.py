from nlp100.helpers import string_helper


def q00(word) -> str:
    return string_helper.reverse(word)


def q01(word) -> str:
    return string_helper.odd(word)


def q02(first, second) -> str:
    return string_helper.alternate(first, second)
