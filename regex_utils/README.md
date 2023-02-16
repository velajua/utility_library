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

