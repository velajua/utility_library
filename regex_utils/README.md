# regex_utils

A module with regex functions to validate strings, clean them and create validators.

Regular expressions (regex) are a sequence of characters that form a pattern. They are used to search, manipulate, and validate text. A regex engine takes a regex pattern and applies it to a string, looking for matches or specific patterns within the string.

Regex allows you to perform complex text searches and manipulations with just a few characters. It can match patterns such as digits, letters, specific characters, and more. You can also use special characters such as the dot (.) to match any character, or the asterisk (*) to match zero or more occurrences of the preceding character.

Regex patterns are created using a set of metacharacters, which have special meanings. For example, the caret (^) is used to match the start of a string, and the dollar sign ($) is used to match the end of a string. These metacharacters can be combined with other characters to create more complex patterns.

Regex is widely used in programming languages and text editors for tasks such as search and replace, input validation, and data parsing. It is a powerful tool for working with text and can be a valuable skill for anyone working with data or programming.

## Installation

To install the required packages, run:

pip install -r requirements.txt

## Usage

### `validator`

A decorator function that takes a regular expression pattern and returns a
function that checks if the given pattern matches the input string.
If `extract` is True, the function returns the matching text,
otherwise it returns True if there is a match, False otherwise.
    
```python
def validator(pattern: str, extract: bool = False) -> callable:
    """
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
```

### `make_validator`

A function that takes a regular expression pattern and returns a
function that checks if the given pattern matches the input string.
If `extract` is True, the function returns the matching text,
otherwise it returns True if there is a match, False otherwise.
    
```python
def make_validator(pattern: str) -> callable:
    """
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
```

### `is_alpha`

A function that checks if the input string contains only alphabetic characters.
    
```python
def is_alpha(string: str, extract: bool = False
             ) -> Union[bool, str]:
    """
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
```

### `is_numeric`

A function that checks if a string is numeric.
    
```python
def is_numeric(string: str, extract: bool = False) -> Union[bool, str]:
    """
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
```

### `is_alphanumeric`

A function that checks if a string is alphanumeric.

```python
def is_alphanumeric(string: str, extract: bool = False
                    ) -> Union[bool, str]:
    """
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
```

### `is_valid_email`

A function that checks if a string is a valid email.

```python
def is_valid_email(email: str, extract: bool = False
                   ) -> Union[bool, str]:
    """
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
```

### `is_valid_url`

A function that checks whether the given URL is valid or not.

```python
def is_valid_url(url: str, extract: bool = False
                 ) -> Union[bool, str]:
    """
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
```

### `is_valid_phone_number_e164`

A function that checks whether the given phone number is valid or not in E.164 format.

```python
def is_valid_phone_number_e164(
        phone_number: str, extract: bool = False) -> Union[bool, str]:
    """
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
```

### `is_valid_postal_code`

A function that checks whether the given postal code is valid or not in India.

```python
def is_valid_postal_code(postal_code: str,
                         extract: bool = False) -> Union[bool, str]:
    """
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
```

### `is_valid_date`

A function that checks whether the given string is a valid date in the format 'YYYY-MM-DD'.

```python
def is_valid_date(date_string: str,
                  extract: Optional[bool] = False) -> Union[bool, str]:
    """
    Args:
        date_string: A string representing a date.
        extract: If True, returns the extracted match instead of a boolean.
    Returns:
        If `extract` is True, returns the matched date string,
            else returns a boolean indicating whether the given string
            is a valid date in the format 'YYYY-MM-DD'.
    """
```

### `is_valid_time`

A function that checks if the input string is a valid time in the format 'HH:MM:SS'.

```python
def is_valid_time(time_string: str, extract: bool = False) -> Union[bool, str]:
    """
    Args:
        time_string (str): The string to be validated.
        extract (bool): If True, returns the matched time string.

    Returns:
        bool or str: If the string is a valid time, returns True.
        If extract is True and
        the string is a valid time, returns the matched time string.
        Otherwise, returns False.
    """
```

### `is_valid_datetime`

A function that checks if the input string is a valid datetime in the format
'YYYY-MM-DD HH:MM:SS'.

```python
def is_valid_datetime(datetime_string: str,
                      extract: bool = False) -> Union[bool, str]:
    """
    Args:
        datetime_string (str): The string to be validated.
        extract (bool): If True, returns the matched datetime string.

    Returns:
        bool or str: If the string is a valid datetime, returns True.
        If extract is True and
        the string is a valid datetime, returns the matched datetime string.
        Otherwise, returns False.
    """
```

### `is_valid_ipv4`

A function that checks if the input string is a valid IPv4 address in the format 'X.X.X.X'.

```python
def is_valid_ipv4(ip_string: str, extract: bool = False) -> Union[bool, str]:
    """
    Args:
        ip_string (str): The string to be validated.
        extract (bool): If True, returns the matched IP string.

    Returns:
        bool or str: If the string is a valid IPv4 address,
        returns True. If extract is True and
        the string is a valid IP address, returns the matched IP string.
        Otherwise, returns False.
    """
```

### `is_valid_ipv6`

A function that checks if the input string is a valid IPv6 address.

```python
def is_valid_ipv6(ip_string: str, extract: bool = False) -> Union[bool, str]:
    """
    Args:
        ip_string (str): The string to be validated.
        extract (bool): If True, returns the matched IP string.

    Returns:
        bool or str: If the string is a valid IPv6 address,
        returns True. If extract is True and
        the string is a valid IP address, returns the matched IP string.
        Otherwise, returns False.
    """
```

### `remove_symbols`

A function that removes symbols from a string.

```python
def remove_symbols(x: str) -> str:
    """
    :param x: The input string
    :type x: str
    :return: The input string with symbols removed
    :rtype: str
    """
```

### `remove_spaces`

A function that removes all whitespaces from a string.

```python
def remove_spaces(x: any) -> str:
    """
    :param x: The value to remove spaces from
    :type x: any
    :return: The input value with all spaces removed
    :rtype: str
    """
```

### `separate_numbers_letters`

A function that separates numbers and letters in a string by adding a space between them.

```python
def separate_numbers_letters(x: str) -> str:
    """
    :param x: The input string
    :type x: str
    :return: The modified string with numbers and
        letters separated by a space
    :rtype: str
    """
```
