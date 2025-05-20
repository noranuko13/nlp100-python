from nlp100.helpers import string_helper
from typing import cast, Dict, List, Set
from string import Template


def q00(first, second) -> str:
    return string_helper.alternate(first, second)


def q01_odd(word) -> str:
    return string_helper.odd(word)


def q01_even(word) -> str:
    return string_helper.even(word)


def q02(word) -> str:
    return string_helper.reverse(word)


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
    return cast(List[List[str]], string_helper.n_gram(words, 2))


def q05_char(text) -> List[str]:
    return cast(List[str], string_helper.n_gram(text, 2))


def q06_union(x, y) -> Set[str]:
    return x.union(y)


def q06_intersection(x, y) -> Set[str]:
    return x.intersection(y)


def q06_symmetric_difference(x, y) -> Set[str]:
    xy = x.difference(y)
    yx = y.difference(x)
    return xy.union(yx)


def q07_template(time, subject, complement) -> str:
    template = Template('$time時の$subjectは$complement')
    return template.substitute(time=time, subject=subject, complement=complement)


def q08(text) -> str:
    return string_helper.cipher(text)


def q09(text) -> str:
    return string_helper.typoglycemia(text)
