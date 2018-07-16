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

    characters = []
    for f, s in zip(first, second):
        characters += f + s

    return ''.join(characters)
