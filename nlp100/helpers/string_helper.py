from typing import List
from typing import Union
import re
import string


def reverse(text) -> str:
    """
    Reverse order of characters in a string.
    Semordnilap, Palindrome, etc.

    :param str text: Text to be reversed.
    :rtype: str
    :return: Reversed text.
    """
    return text[::-1]


def odd(text) -> str:
    """
    Get Odd-numbered characters.

    :param str text: String to convert.
    :rtype: str
    :return: String combining odd-numbered characters.
    """
    return text[::2]


def even(text) -> str:
    """
    Get Even-numbered characters.

    :param str text: String to convert.
    :rtype: str
    :return: String combining even-numbered characters.
    """
    return text[1::2]


def alternate(first, second) -> str:
    """
    Combine two words alternately.
    TODO: 「はむみしがばき」「ブシャラモシジ」
          different length, Yōon (拗音)

    :param first: First word.
    :param second: Second word.
    :rtype: str
    :return: The result of string (ひとつとびぶったい).
    """
    if len(first) != len(second):
        raise ValueError('Different length strings not available.')

    characters = []  # type: List[str]
    for f, s in zip(first, second):
        characters += f + s

    return ''.join(characters)


def remove_punctuation(text) -> str:
    """
    Get String without Punctuation Symbol.

    :param str text: String to convert.
    :rtype: str
    :return: String without Punctuation.
    """
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)


def split_into_words(text) -> List[str]:
    """
    Convert text into word list.
    Delimiter: Half-width Space.

    :param str text: Text to be converted into words.
    :rtype: List[str]
    :return: Converted word list.
    """
    text = text.strip()
    pattern = re.compile(r'[{0}]+'.format(string.whitespace))
    text = re.sub(pattern, ' ', text)

    if len(text) == 0:
        return []

    return text.split(' ')


def n_gram(target, n) -> Union[List[str], List[List[str]]]:
    """
    Generate N-gram.

    :param target: Words or Word lists to be converted into N-gram.
    :param int n: Number of characters per n-gram.
    :return: N-gram.
    """
    return [target[i:i + n] for i in range(0, len(target) - n + 1)]
