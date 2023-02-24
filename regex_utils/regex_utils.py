import re
import unidecode

from typing import Union, Optional


def validator(pattern: str, extract: bool = False) -> callable:
    """
    A decorator function that takes a regular expression pattern
    and returns a function that checks if the given pattern matches
    the input string. If `extract` is True, the function returns
    the matching text, otherwise it returns True if there is a match,
    False otherwise.

    Args:
    - pattern (str): A regular expression pattern
    - extract (bool): Whether to extract the matching text
        or not (default: False)

    Returns:
    - callable: A function that checks if the given pattern
        matches the input string

    Examples:
    >>> @validator(r'^\d+$')
    ... def is_number(num: str) -> bool:
    ...     return True
    >>> is_number('123')
    True
    >>> is_number('abc')
    False
    """

    def decorator(func: callable) -> callable:
        def wrapper(text: str) -> Union[bool, str]:
            pattern_ = pattern[1:-1] if extract else pattern
            match = re.search(pattern_, text)
            return match.group() if extract and match else bool(match)
        return wrapper
    return decorator


def make_validator(pattern: str) -> callable:
    """
    A function that takes a regular expression pattern and
    returns a function that checks if the given pattern matches
    the input string. If `extract` is True, the function returns
    the matching text, otherwise it returns True if there is a match,
    False otherwise.

    Args:
    - pattern (str): A regular expression pattern

    Returns:
    - callable: A function that checks if the given pattern
        matches the input string

    Examples:
    >>> is_alpha = make_validator(r'^[a-zA-Z]+$')
    >>> is_alpha('abcd')
    True
    >>> is_alpha('123')
    False
    """

    def validator(text: str, extract: bool = False) -> Union[bool, str]:
        pattern_ = pattern[1:-1] if extract else pattern
        match = re.search(pattern_, text)
        return match.group() if extract and match else bool(match)
    return validator


def is_alpha(string: str, extract: bool = False
             ) -> Union[bool, str]:
    """
    A function that checks if the input string contains
    only alphabetic characters.

    Args:
    - string (str): The input string
    - extract (bool): Whether to extract the matching text
        or not (default: False)

    Returns:
    - Union[bool, str]: True if the input string contains
        only alphabetic characters, False otherwise.
        If `extract` is True and there is a match,
        the function returns the matching text.

    Examples:
    >>> is_alpha('abcd')
    True
    >>> is_alpha('123')
    False
    """

    pattern = r'^[a-zA-Z]+$'
    return make_validator(pattern)(string, extract)


def is_numeric(string: str, extract: bool = False) -> Union[bool, str]:
    """Check if a string is numeric.

    Args:
        string: The string to be checked.
        extract: If True, the matched numeric string will be returned.
            If False, a boolean indicating if the string is
            numeric will be returned.

    Returns:
        If `extract` is True and the string is numeric,
            the matched numeric string will be returned.
        If `extract` is False and the string is numeric, True
            will be returned. Otherwise, False will be returned.

    """
    pattern = r'^-?\d*\.?\d+$'
    if extract:
        pattern = pattern[1:-1]
    match = re.search(pattern, string)
    if extract and match:
        return match.group()
    return bool(match)


def is_alphanumeric(string: str, extract: bool = False
                    ) -> Union[bool, str]:
    """Check if a string is alphanumeric.

    Args:
        string: The string to be checked.
        extract: If True, the matched alphanumeric string will
            be returned. If False, a boolean indicating if the
            string is alphanumeric will be returned.

    Returns:
        If `extract` is True and the string is alphanumeric,
            the matched alphanumeric string will be returned.
        If `extract` is False and the string is alphanumeric,
            True will be returned. Otherwise, False will be returned.

    """
    pattern = r'^[a-zA-Z0-9]+$'
    if extract:
        pattern = pattern[1:-1]
    match = re.search(pattern, string)
    if extract and match:
        return match.group()
    return bool(match)


def is_valid_email(email: str, extract: bool = False
                   ) -> Union[bool, str]:
    """Check if a string is a valid email.

    Args:
        email: The string to be checked.
        extract: If True, the matched email will be returned.
        If False, a boolean indicating if the string is a
        valid email will be returned.

    Returns:
        If `extract` is True and the string is a valid email,
            the matched email will be returned.
        If `extract` is False and the string is a valid email,
            True will be returned. Otherwise, False will be returned.

    """
    pattern = r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if extract:
        pattern = pattern[1:-1]
    match = re.search(pattern, email)
    if extract and match:
        return match.group()
    return bool(match)


def is_valid_url(url: str, extract: bool = False
                 ) -> Union[bool, str]:
    """
    Checks whether the given URL is valid or not.

    Args:
    - url: A string representing the URL to be validated.
    - extract: A boolean indicating whether to return the
        matched portion of the URL instead of a boolean value.
        Default is False.

    Returns:
    - If extract is True, returns the matched portion
        of the URL if it exists, otherwise returns False.
    - If extract is False, returns a boolean value
        indicating whether the given URL is valid or not.
    """
    pattern = r'^(https?://)?(?:[-\w.]|(?:%[\da-fA-F]{2}))+/?[\w.-]*$'
    if extract:
        pattern = pattern[1:-1]
    match = re.search(pattern, url)
    if extract and match:
        return match.group()
    return bool(match)


def is_valid_phone_number_e164(
        phone_number: str, extract: bool = False) -> Union[bool, str]:
    """
    Checks whether the given phone number is valid or not in E.164 format.

    Args:
    - phone_number: A string representing the phone number to be validated.
    - extract: A boolean indicating whether to return the matched
        portion of the phone number instead of a boolean value.
        Default is False.

    Returns:
    - If extract is True, returns the matched portion of the
        phone number if it exists, otherwise returns False.
    - If extract is False, returns a boolean value indicating
        whether the given phone number is valid or not.
    """
    pattern = r'^\+[1-9]\d{8,14}$'
    if extract:
        pattern = pattern[1:-1]
    match = re.search(pattern, phone_number)
    if extract and match:
        return match.group()
    return bool(match)


def is_valid_postal_code(postal_code: str,
                         extract: bool = False) -> Union[bool, str]:
    """
    Checks whether the given postal code is valid or not in India.

    Args:
    - postal_code: A string representing the postal code to be validated.
    - extract: A boolean indicating whether to return the matched
        portion of the postal code instead of a boolean value.
        Default is False.

    Returns:
    - If extract is True, returns the matched portion of the postal code if it
      exists, otherwise returns False.
    - If extract is False, returns a boolean value indicating whether the given
      postal code is valid or not.
    """
    pattern_range = r'^[1-9]\d{5}$'
    pattern_pair = r'(\d)(?=\d\1)'
    if extract:
        pattern_range = pattern_range[1:-1]
    match_range = re.search(pattern_range, str(postal_code))
    match_pair = len(re.findall(pattern_pair, str(postal_code))) < 2
    if extract and match_range and match_pair:
        return match_range.group()
    return bool(match_range and match_pair)


def is_valid_date(date_string: str,
                  extract: Optional[bool] = False) -> Union[bool, str]:
    """Checks whether the given string is a valid date in the format 'YYYY-MM-DD'.

    Args:
        date_string: A string representing a date.
        extract: If True, returns the extracted match instead of a boolean.

    Returns:
        If `extract` is True, returns the matched date string,
            else returns a boolean indicating whether the given string
            is a valid date in the format 'YYYY-MM-DD'.
    """
    pattern = r'^\d{4}-\d{2}-\d{2}$'
    if extract:
        pattern = pattern[1:-1]
    match = re.search(pattern, date_string)
    if extract and match:
        return match.group()
    return bool(match)


def is_valid_time(time_string: str, extract: bool = False) -> Union[bool, str]:
    """
    Check if the input string is a valid time in the format 'HH:MM:SS'.

    Args:
        time_string (str): The string to be validated.
        extract (bool): If True, returns the matched time string.

    Returns:
        bool or str: If the string is a valid time, returns True.
        If extract is True and
        the string is a valid time, returns the matched time string.
        Otherwise, returns False.
    """
    pattern = r'^\d{2}:\d{2}:\d{2}$'
    if extract:
        pattern = pattern[1:-1]
    match = re.search(pattern, time_string)
    if extract and match:
        return match.group()
    return bool(match)


def is_valid_datetime(datetime_string: str,
                      extract: bool = False) -> Union[bool, str]:
    """
    Check if the input string is a valid datetime in the format
    'YYYY-MM-DD HH:MM:SS'.

    Args:
        datetime_string (str): The string to be validated.
        extract (bool): If True, returns the matched datetime string.

    Returns:
        bool or str: If the string is a valid datetime, returns True.
        If extract is True and
        the string is a valid datetime, returns the matched datetime string.
        Otherwise, returns False.
    """
    pattern = r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$'
    if extract:
        pattern = pattern[1:-1]
    match = re.search(pattern, datetime_string)
    if extract and match:
        return match.group()
    return bool(match)


def is_valid_ip(ip_string: str, extract: bool = False) -> Union[bool, str]:
    """
    Check if the input string is a valid IPv4 address in the format 'X.X.X.X'.

    Args:
        ip_string (str): The string to be validated.
        extract (bool): If True, returns the matched IP string.

    Returns:
        bool or str: If the string is a valid IPv4 address,
        returns True. If extract is True and
        the string is a valid IP address, returns the matched IP string.
        Otherwise, returns False.
    """
    pattern = r'^(?:(?:1?\d{1,2}|2[0-4]\d|25[0-5])\.){3}(?:1?\d{1,2}|2[0-4]\d|25[0-5])$'
    if extract:
        pattern = pattern[1:-1]
    match = re.search(pattern, ip_string)
    if extract and match:
        return match.group()
    return bool(match)


def remove_symbols(x: str) -> str:
    """
    A function that removes symbols from a string
    :param x: The input string
    :type x: str
    :return: The input string with symbols removed
    :rtype: str
    """
    x = unidecode(x) if x else ''
    return re.sub(r'[^\w ]', '', x)


def remove_spaces(x: any) -> str:
    """
    A function that removes all whitespaces from a string
    :param x: The value to remove spaces from
    :type x: any
    :return: The input value with all spaces removed
    :rtype: str
    """
    return re.sub(r'\s', '', str(x))


def separate_numbers_letters(x: str) -> str:
    """
    A function that separates numbers and letters
    in a string by adding a space between them
    :param x: The input string
    :type x: str
    :return: The modified string with numbers and
        letters separated by a space
    :rtype: str
    """
    return ' '.join(re.findall(
        '[0-9]+|[a-zA-Z]+', x))
