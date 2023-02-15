# utils

A module with various decorators and everyday functions.

In Python, a decorator is a special type of function that can modify or enhance the behavior of another function or class without changing its source code. A decorator is a higher-order function that takes another function as input and returns a new function that adds some additional behavior to the original function. Decorators are a key feature of Python and are commonly used in many frameworks and libraries.

Decorators are defined using the "@" symbol followed by the name of the decorator function. The decorator function takes a single argument, which is the function or class being decorated. The decorator function then returns a new function or class that wraps the original function or class and adds some additional behavior.

## Installation

To install the required packages, run:

pip install -r requirements.txt

# Usage

## Decorators

### `retry_decorator`

A decorator that allows a function to retry a specified number of times in case of an exception

```python
def retry_decorator(max_retries: int) -> Callable:
    """
    use: @retry_decorator(tries)
    :param max_retries: The maximum number of times to retry
    :type max_retries: int
    :return: The decorated function
    :rtype: Callable
    """
```

### `timed_retries`

 A decorator that allows a function to retry a specified number of times after a specified time interval in case of an exception
    
```python
def timed_retries(max_retries: int,
                  minutes: int = 1) -> Callable:
    """
    use: @timed_retries(tries, wait_mins)
    :param max_retries: The maximum number of times to retry
    :type max_retries: int
    :param minutes: The time interval between retries in minutes
    :type minutes: int
    :return: The decorated function
    :rtype: Callable
    """
```

### `exit_after`

A decorator that exits the program if the function takes more than seconds seconds

```python
def exit_after(seconds: int) -> Callable:
    """
    use: @exit_after(seconds)
    :param seconds: The time limit in seconds
    :type seconds: int
    :return: The decorated function
    :rtype: Callable
    """
```

### `execution_time`

A decorator that calculates the execution time of a function

```python
def execution_time(f: Callable) -> Callable:
    """
    use: @execution_time
    :param f: The function to be decorated
    :type f: Callable
    :return: The decorated function
    :rtype: Callable
    """
```

### `remove_duplicates`

A decorator that removes duplicates from a list passed to the decorated function

```python
def remove_duplicates(f: Callable) -> Callable:
    """
    use: @remove_duplicates
    :param f: The function to be decorated
    :type f: Callable
    :return: The decorated function
    :rtype: Callable
    """
```

## Functions

### `levenshtein`

A function that calculates the Levenshtein distance (or edit distance) between two strings.
The Levenshtein distance is the minimum number of single-character edits (insertions, deletions or substitutions)
required to change one string into the other.

```python
def levenshtein(word1: str, word2: str) -> int:
    """
    :param word1: The first string
    :type word1: str
    :param word2: The second string
    :type word2: str
    :return: The Levenshtein distance between word1 and word2
    :rtype: int
    """
```

### `category_mapper`

A function that maps the elements of a list to the closest matching elements in a master list.

```python
def category_mapper(master_list: List[str],
                    list_to_map: List[str],
                    type_: str = 'both') -> Union[
                        Tuple[List[str], List[str]], List[str]]:
    """
    :param master_list: The master list to map the
        elements of list_to_map to
    :type master_list: List[str]
    :param list_to_map: The list to map the elements
        of to the master list
    :type list_to_map: List[str]
    :param type_: The type of output to return,
        can be 'both' (default), 'ans', or 'filled'
    :type type_: str
    :return: A tuple of two lists (ans, filled) if type_ is 'both',
        or a list of matched elements if type_ is 'ans' or 'filled'
    :rtype: Union[Tuple[List[str], List[str]], List[str]]
    """
```

### `find_rank`

A function that finds the lexicographic rank of a string.

```python
def find_rank(st: str) -> int:
    """
    :param st: The string to find the rank of
    :type st: str
    :return: The lexicographic rank of the string
    :rtype: int
    """
```

### `check_value`

A function that checks if a value is not None, returns a tuple containing the value and a boolean.
    
```python
def check_value(x: any, default: any = None
                ) -> Tuple[any, bool]:
    """
    indicating if the value is not None
    :param x: The value to check
    :type x: any
    :param default: The default value to return
        if x is None
    :type default: any
    :return: A tuple containing the value and a boolean
        indicating if the value is not None
    :rtype: Tuple[any, bool]
    """
```

### `int_safe_cast`

A function that safely converts a value to int and returns None if the conversion is not possible.
    
```python
def int_safe_cast(x: any) -> Union[int, None]:
    """
    :param x: The value to convert
    :type x: any
    :return: The converted int value or None
    :rtype: Union[int, None]
    """
```

### `float_safe_cast`

A function that safely converts a value to float and returns None if the conversion is not possible.
    
```python
def float_safe_cast(x: any) -> Union[float, None]:
    """
    A function that safely converts a value to float
    and returns None if the conversion is not possible
    :param x: The value to convert
    :type x: any
    :return: The converted float value or None
    :rtype: Union[float, None]
    """
```

### `word_replacer`

A function that replaces words in a sentence with the corresponding values from the provided data dictionary.
    
```python
def word_replacer(sentence: str,
                  data: Dict[str, str]) -> str:
    """
    :param sentence: The input sentence
    :type sentence: str
    :param data: A dictionary containing the words to be
        replaced as keys and their replacement values as values
    :type data: Dict[str, str]
    :return: The modified sentence
    :rtype: str
    """
```

### `combination_powerset`

Returns the powerset of a given set.
The powerset is a set of all subsets of a given set, including the empty set and the original set.
    
```python
def combination_powerset(set_: set) -> set:
    """    
    :param set_: The input set
    :return: The powerset of the input set
    """
```

### `powerset`

Returns the powerset of a given set.
The powerset is a set of all subsets of a given set, including the empty set and the original set.
    
```python
def powerset(set_: set) -> List[List[int]]:
    """    
    :param s: The input set
    :return: The powerset of the input set, as a list of lists
    """
```

### `odd_ones_out`

Returns the characters from string 'new_' that are not present in string 'old_'.
    
```python
def odd_ones_out(old_: str, new_: str) -> str:
    """    
    :param old_: The first input string
    :param new_: The second input string
    :return: The characters in string 'new_' that are not present in string 'old_'
    """
```
