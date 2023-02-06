import os
import re
import sys
import time
import difflib
import unidecode
import threading
import _thread as thread

from math import factorial
from functools import wraps
from datetime import datetime

from typing import Callable, List, Tuple, Union, Dict


def retry_decorator(max_retries: int) -> Callable:
    """
    A decorator that allows a function to retry a
    specified number of times in case of an exception

    use: @retry_decorator(tries)

    :param max_retries: The maximum number of times to retry
    :type max_retries: int
    :return: The decorated function
    :rtype: Callable
    """
    def retry_decorator_(f: Callable) -> Callable:
        @wraps(f)
        def func_with_retries(*args, **kwargs):
            error = None
            count = 0
            for _ in range(max_retries):
                count += 1
                if count > 1:
                    print(f'''retry_decorator for {
                        f.__name__} attempt:''', count)
                try:
                    return f(*args, **kwargs)
                except Exception as e:
                    error = e
                time.sleep(5)
            print(f'''error in {f.__name__} args:{args
                  } kwargs:{kwargs} error:{error}''')
            return None
        return func_with_retries
    return retry_decorator_


def timed_retries(max_retries: int,
                  minutes: int = 1) -> Callable:
    """
    A decorator that allows a function to retry a
    specified number of times after a specified time
    interval in case of an exception

    use: @timed_retries(tries, wait_mins)

    :param max_retries: The maximum number of times to retry
    :type max_retries: int
    :param minutes: The time interval between retries in minutes
    :type minutes: int
    :return: The decorated function
    :rtype: Callable
    """
    def retry_decorator(f: Callable) -> Callable:
        @wraps(f)
        def func_with_retries(*args, **kwargs):
            error = None
            for i in range(max_retries):
                try:
                    print(f'''retry_decorator for {
                        f.__name__} attempt:''', i)
                    return f(*args, **kwargs)
                except Exception as e:
                    time.sleep(60*minutes)
                    error = e
            print(f'''error in {f.__name__} args:{args
                  } kwargs:{kwargs} error:{error}''')
            return None
        return func_with_retries
    return retry_decorator


def exit_after(seconds: int) -> Callable:
    """
    A decorator that exits the program
    if the function takes more than seconds seconds

    use: @exit_after(seconds)

    :param seconds: The time limit in seconds
    :type seconds: int
    :return: The decorated function
    :rtype: Callable
    """
    def quit_function(f_name: str):
        """
        A function that aborts the main thread
        and prints an error message

        :param f_name: The name of the function
            that is being decorated
        :type f_name: str
        """
        print(f'{f_name} aborted', file=sys.stderr)
        sys.stderr.flush()
        thread.interrupt_main()

    def outer(f: Callable) -> Callable:
        @wraps(f)
        def inner(*args, **kwargs):
            timer = threading.Timer(
                seconds, quit_function,
                args=[f.__name__])
            timer.start()
            try:
                result = f(*args, **kwargs)
            finally:
                timer.cancel()
            return result
        return inner
    return outer


def execution_time(f: Callable) -> Callable:
    """
    A decorator that calculates the execution time of a function

    use: @execution_time

    :param f: The function to be decorated
    :type f: Callable
    :return: The decorated function
    :rtype: Callable
    """
    @wraps(f)
    def get_execution_time(*args, **kwargs):
        initial = datetime.now()
        ans = f(*args, **kwargs)
        print(f'''execution time for function "{f.__name__}":
{datetime.now() - initial}\n''')
        return ans
    return get_execution_time


def remove_duplicates(f: Callable) -> Callable:
    """
    A decorator that removes duplicates from
    a list passed to the decorated function

    use: @remove_duplicates

    :param f: The function to be decorated
    :type f: Callable
    :return: The decorated function
    :rtype: Callable
    """
    @wraps(f)
    def func_no_duplicates(*args):
        if type(*args) == list:
            args = list(dict.fromkeys(*args))
        return f(*args)
    return func_no_duplicates


def levenshtein(word1: str, word2: str) -> int:
    """
    A function that calculates the Levenshtein
    distance (or edit distance) between two strings.
    The Levenshtein distance is the minimum number of
    single-character edits (insertions, deletions or substitutions)
    required to change one string into the other.

    :param word1: The first string
    :type word1: str
    :param word2: The second string
    :type word2: str
    :return: The Levenshtein distance between word1 and word2
    :rtype: int
    """
    def min_dist(s1: int, s2: int) -> int:
        """
        A helper function that calculates the minimum
        distance between the two strings
        :param s1: The current position of the pointer in word1
        :type s1: int
        :param s2: The current position of the pointer in word2
        :type s2: int
        :return: The minimum distance between the two strings
        :rtype: int
        """
        if s1 == len(word1):
            return len(word2) - s2
        if s2 == len(word2):
            return len(word1) - s1
        if word1[s1] == word2[s2]:
            return min_dist(s1 + 1, s2 + 1)
        output = 1 + min(min_dist(s1, s2 + 1),
                         min_dist(s1 + 1, s2),
                         min_dist(s1 + 1, s2 + 1))
        return output

    return min_dist(0, 0)


def category_mapper(master_list: List[str],
                    list_to_map: List[str],
                    type_: str = 'both') -> Union[
                        Tuple[List[str], List[str]], List[str]]:
    """
    A function that maps the elements of a list to
    the closest matching elements in a master list
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
    assert type_ in ['both', 'ans', 'filled'
                     ], f'Invalid value for type_: {type_}'
    ans, filled = [], []
    for i in list_to_map:
        match = difflib.get_close_matches(i, master_list)
        ans.append(match[0] if match else '')
        filled.append(match[0] if match else i)
    if type_ == 'both':
        return ans, filled
    elif type_ == 'ans':
        return ans
    elif type_ == 'filled':
        return filled


def find_rank(st: str) -> int:
    """
    A function that finds the lexicographic rank of a string
    :param st: The string to find the rank of
    :type st: str
    :return: The lexicographic rank of the string
    :rtype: int
    """
    def find_smaller_right(st: str, low: int,
                           high: int) -> int:
        """
        A helper function that finds the number of characters
        that are smaller than the character at the left index
        :param st: The input string
        :type st: str
        :param low: The left index
        :type low: int
        :param high: The right index
        :type high: int
        :return: The number of characters that are
            smaller than the character at the left index
        :rtype: int
        """
        count_r = 0
        i = low + 1
        while i <= high:
            if st[i] < st[low]:
                count_r += 1
            i += 1
        return count_r

    ln = len(st)
    mul = factorial(ln)
    rank, i = 1, 0
    while i < ln:
        mul = mul // (ln - i)
        count_r = find_smaller_right(st, i, ln - 1)
        rank += count_r * mul
        i += 1
    return rank


def remove_symbols(x: str) -> str:
    """
    A function that removes symbols from a string
    :param x: The input string
    :type x: str
    :return: The input string with symbols removed
    :rtype: str
    """
    # Removes accents and other diacritical marks
    # from the string
    x = unidecode.unidecode(x)
    return re.sub(r'[^\w ]', '', x)


def check_value(x: any, default: any = None
                ) -> Tuple[any, bool]:
    """
    A function that checks if a value is not None,
    returns a tuple containing the value and a boolean
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
    return (x, True) if x else (default, False)


def int_safe_cast(x: any) -> Union[int, None]:
    """
    A function that safely converts a value to int
    and returns None if the conversion is not possible
    :param x: The value to convert
    :type x: any
    :return: The converted int value or None
    :rtype: Union[int, None]
    """
    if x is not None:
        # Removes all non-numeric characters
        # from the input value
        x = re.sub('[^0-9.-]', '', str(x))
        # Removes the decimal part of the input value
        x = x.partition('.')[0]
        if x.isnumeric():
            return int(x)
    return None


def float_safe_cast(x: any) -> Union[float, None]:
    """
    A function that safely converts a value to float
    and returns None if the conversion is not possible
    :param x: The value to convert
    :type x: any
    :return: The converted float value or None
    :rtype: Union[float, None]
    """
    if x is not None:
        # Removes all non-numeric characters
        # from the input value
        x = re.sub('[^0-9.-]', '', str(x))
        try:
            return float(x)
        except Exception:
            return None
    return None


def remove_spaces(x: any) -> str:
    """
    A function that removes all whitespaces from a string
    :param x: The value to remove spaces from
    :type x: any
    :return: The input value with all spaces removed
    :rtype: str
    """
    return re.sub(r'\s', '', str(x))


def word_replacer(sentence: str,
                  data: Dict[str, str]) -> str:
    """
    A function that replaces words in a sentence with the
    corresponding values from the provided data dictionary.
    :param sentence: The input sentence
    :type sentence: str
    :param data: A dictionary containing the words to be
        replaced as keys and their replacement values as values
    :type data: Dict[str, str]
    :return: The modified sentence
    :rtype: str
    """
    for k, v in data.items():
        sentence = re.sub(fr'(?:\s+|^){k}(?:\s+|$)',
                          f' {v} ', sentence)
    return sentence.strip()


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


file_name = os.path.splitext(os.path.basename(os.path.abspath(__file__)))[0]
dir_name = os.path.basename(os.path.dirname(os.path.abspath(__file__)))
if __name__ == "__main__" or __name__ == f"{dir_name}.{file_name}":
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
