import os
import sys
import dill
import redis
import pickle

from typing import Union, Optional


def redis_set(key: str, value: str,
              replace: Optional[bool]=True,
              days: Optional[int]=None):
    """
    Set the value of the key in Redis. If the key already exists,
    the value is either replaced or not, depending on the value
    of the `replace` argument.
    :param key: Key of the value to be stored
    :param value: Value to be stored
    :param replace: If True, replace the value
      if the key already exists.
                    If False, return False
      if the key already exists.
                    Default is True.
    :param days: Expiration time in days,
      if None it will never expire
    :return: True if the value was successfully set,
      False if the key already exists and `replace` is False
    """
    if redis_client.exists(key) and not replace:
        return False
    redis_client.set(key, value)
    if days:
        redis_client.expire(key, 60 * 60 * 24 * days)
    return True


def redis_get(key: str) -> Union[str, None]:
    """
    Get the value of the key in Redis
    :param key: Key of the value to be retrieved
    :return: The value stored in Redis,
      None if the key does not exist
    """
    if redis_client.exists(key):
        return redis_client.get(key).decode('utf-8')
    return None


def redis_ttl(key: str) -> int:
    """
    Get the remaining time to live in seconds for
    the given key in Redis
    :param key: Key of the value to be retrieved
    :return: The time to live for the key in Redis,
      -1 if the key does not exist
    """
    if redis_client.exists(key):
        return redis_client.ttl(key)
    return -1


def redis_set_dill(key: str, df, days: Optional[int]=None):
    """
    Store a Python object using dill serialization in Redis
    :param key: Key of the object to be stored
    :param df: Object to be stored
    :param days: Expiration time in days,
      if None it will never expire
    :return: True if the object was stored successfully
    """
    redis_client.set(key, dill.dumps(df))
    if days:
        redis_client.expire(key, 60 * 60 * 24 * days)
    return True


def redis_get_dill(key: str) -> Union[object, None]:
    """
    Retrieve a Python object stored in Redis
    using dill serialization
    :param key: Key of the object to be retrieved
    :return: The object stored in Redis,
      None if the key does not exist
    """
    if redis_client.exists(key):
        return dill.loads(redis_client.get(key))
    return None


def redis_set_df(key: str, df: Any,
                 days: Optional[int]=None) -> bool:
    """
    Function to store a pandas dataframe in Redis cache.
    
    Parameters:
    key (str): Key to store the dataframe under in Redis.
    df (Any): Data to be stored, can be any type
      that is serializable.
    days (int, optional): Number of days until the
      key-value pair expires. Defaults to None.
    Returns:
    bool: Returns True if the data was stored successfully,
      False otherwise.
    """
    redis_client.set(key, pickle.dumps(df))
    if days:
        redis_client.expire(key, 60 * 60 * 24 * days)
    return True


def redis_get_df(key: str) -> Optional[Any]:
    """
    Function to retrieve a stored pandas dataframe
    from Redis cache.
    
    Parameters:
    key (str): Key to retrieve the dataframe from in Redis.
    Returns:
    Any: Returns the deserialized dataframe
      if it exists, None otherwise.
    """
    if redis_client.exists(key):
        return pickle.loads(redis_client.get(key))
    return None


def cache_redis(key, value, millis):
    redis_client.psetex(key, millis, value)


file_name = os.path.splitext(os.path.basename(os.path.abspath(__file__)))[0]
dir_name = os.path.basename(os.path.dirname(os.path.abspath(__file__)))
if __name__ == "__main__" or __name__ == f"{dir_name}.{file_name}":
    redis_port = 6379
    redis_host = "localhost" # ip of redis host

    redis_client = redis.Redis(host=redis_host, port=redis_port)
