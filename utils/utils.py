import os
import re
import sys
import time
import difflib
import unidecode
import threading
import _thread as thread

from math import factorial
from typing import Callable
from functools import wraps
from datetime import datetime


def retry_decorator(max_retries: int) -> Callable:
    """
    A decorator that allows a function to retry a
    specified number of times in case of an exception

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



def timed_retries(max_retries, minutes=1):
    def retry_decorator(f):
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


def exit_after(s):
    def quit_function(f_name):
        print(f'{f_name} aborted', file=sys.stderr)
        sys.stderr.flush()
        thread.interrupt_main()

    def outer(f):
        @wraps(f)
        def inner(*args, **kwargs):
            timer = threading.Timer(s, quit_function,
                                    args=[f.__name__])
            timer.start()
            try:
                result = f(*args, **kwargs)
            finally:
                timer.cancel()
            return result
        return inner
    return outer


def execution_time(f):
    @wraps(f)
    def get_execution_time(*args, **kwargs):
        initial = datetime.now()
        ans = f(*args, **kwargs)
        print(f'''execution time for function "{f.__name__}":
{datetime.now() - initial}\n''')
        return ans
    return get_execution_time


def remove_duplicates(f):
    @wraps(f)
    def func_no_duplicates(*args):
        if type(*args) == list:
            return f(list(dict.fromkeys(*args)))
        return f(*args)
    return func_no_duplicates


def levenshtein(word1, word2):
    def min_dist(s1, s2):
        if s1 == len(word1) or s2 == len(word2):
            return len(word1) - s1 + len(word2) - s2
        if word1[s1] == word2[s2]:
            return min_dist(s1+1, s2+1)
        output = 1 + min(min_dist(s1, s2+1),
                         min_dist(s1+1, s2),
                         min_dist(s1+1, s2+1))
        return output

    return min_dist(0, 0)


def category_mapper(master_list, list_to_map, type_='both'):
    assert type_ in ['both', 'ans',
                     'filled'], 'Not a value for type_'
    ans, filled = [], []
    for i in list_to_map:
        ans.append(value_[0] if (
            value_ := difflib.get_close_matches(
                i, master_list)) else '')
        filled.append(value_[0] if value_ else i)
    if type_ == 'both':
        return ans, filled
    elif type_ == 'ans':
        return ans
    elif type_ == 'filled':
        return filled


def find_rank(st):
    def find_smaller_right(st, low, high):
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


def remove_symbols(x):
    x = unidecode.unidecode(x)
    return re.sub(r'[^\w ]', '', x)


def check_value(x, default=None):
    return (x, True) if x else (default, False)


def int_safe_cast(x):
    if x is not None:
        x = re.sub('[^0-9.-]', '', str(x))
        x = x.partition('.')[0]
        if x.isnumeric():
            return int(x)
    return None


def float_safe_cast(x):
    if x is not None:
        x = re.sub('[^0-9.-]', '', str(x))
        try:
            return float(x)
        except:
            return None
    return None


def remove_spaces(x):
    return re.sub('\s', '', str(x))


def word_replacer(sentence, data):
    for k, v in data.items():
        sentence = re.sub(f'(?:\s+|^){k}(?:\s+|$)',
                          f' {v} ', sentence)
    return sentence


def separate_numbers_letters(x):
    return ' '.join(re.findall(
        '[0-9]+|[a-zA-Z]+', x))


file_name = os.path.splitext(os.path.basename(os.path.abspath(__file__)))[0]
dir_name = os.path.basename(os.path.dirname(os.path.abspath(__file__)))
if __name__ == "__main__" or __name__ == f"{dir_name}.{file_name}":
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
