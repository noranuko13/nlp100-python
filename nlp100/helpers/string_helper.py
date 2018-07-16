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
