# redis_utils

A module with Redis functions to store and retrieve values and objects. 
to create a Redis instance, follow [`this link`](https://redis.io/docs/getting-started/installation/).

Redis is an open-source, in-memory data structure store that can be used as a database, cache, and message broker. It supports various data structures such as strings, hashes, sets, lists, and sorted sets, and provides a rich set of commands to operate on these data structures.

Redis is often used as a fast, reliable, and scalable caching solution, due to its ability to store data entirely in memory, which makes it much faster than disk-based databases. It also provides features such as data persistence and replication for improved reliability and availability.

Some of the key features of Redis include:

High performance: Redis is designed to be extremely fast, with the ability to perform millions of operations per second.
Data structures: Redis supports a variety of data structures, including strings, hashes, sets, lists, and sorted sets, which can be used to store and manipulate data in a flexible way.
Persistence: Redis provides various mechanisms to persist data to disk, including snapshotting and append-only files.
Replication: Redis supports master-slave replication, allowing multiple Redis instances to be used for improved availability and scalability.
Lua scripting: Redis allows Lua scripts to be executed directly on the server, which can be used to implement complex data manipulations or transactions.
Redis can be accessed through a number of client libraries in various programming languages, including Python, Java, Ruby, and Node.js. The Redis commands can be sent to Redis server through the client libraries and responses can be received and parsed back.

Overall, Redis is a versatile and powerful tool for managing and storing data, and can be used in a wide range of applications, including web applications, mobile apps, and Internet of Things (IoT) devices.

## Installation

To install the required packages, run:

pip install -r requirements.txt

## Usage

### `redis_set`

Set the value of the key in Redis. If the key already exists, the value is either replaced or not, depending on the value of the `replace` argument.
    
```python
def redis_set(key: str, value: str,
              replace: Optional[bool]=True,
              days: Optional[int]=None):
    """
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
```

### `redis_get`

Get the value of the key in Redis

```python
def redis_get(key: str) -> Union[str, None]:
    """
    :param key: Key of the value to be retrieved
    :return: The value stored in Redis,
      None if the key does not exist
    """
```

### `redis_ttl`

Get the remaining time to live in seconds for the given key in Redis.

```python
def redis_ttl(key: str) -> int:
    """
    :param key: Key of the value to be retrieved
    :return: The time to live for the key in Redis,
      -1 if the key does not exist
    """
```

### `redis_set_dill`

Store a Python object using dill serialization in Redis.

```python
def redis_set_dill(key: str, df: Any,
                   replace: Optional[bool]=True,
                   days: Optional[int]=None):
    """
    :param key: Key of the object to be stored
    :param df: Object to be stored
    :param replace: If True, replace the value
      if the key already exists.
                    If False, return False
      if the key already exists.
                    Default is True.
     :param days: Expiration time in days,
      if None it will never expire
    :return: True if the object was stored successfully
    """
```

### `redis_get_dill`

Retrieve a Python object stored in Redis using dill serialization.

```python
def redis_get_dill(key: str) -> Union[object, None]:
    """
    :param key: Key of the object to be retrieved
    :return: The object stored in Redis,
      None if the key does not exist
    """
```

### `redis_set_df`

Function to store a pandas dataframe in Redis cache.

```python
def redis_set_df(key: str, df: Any,
                 replace: Optional[bool]=True,
                 days: Optional[int]=None) -> bool:
    """    
    Parameters:
    key (str): Key to store the dataframe under in Redis.
    df (Any): Data to be stored, can be any type
      that is serializable.
    replace (bool): If True, replace the value
      if the key already exists.
                    If False, return False
      if the key already exists.
                    Default is True.
    days (int, optional): Number of days until the
      key-value pair expires. Defaults to None.
    Returns:
    bool: Returns True if the data was stored successfully,
      False otherwise.
    """
```

### `redis_get_df`

Function to retrieve a stored pandas dataframe from Redis cache.

```python
def redis_get_df(key: str) -> Optional[Any]:
    """    
    Parameters:
    key (str): Key to retrieve the dataframe from in Redis.
    Returns:
    Any: Returns the deserialized dataframe
      if it exists, None otherwise.
    """
```

### `cache_redis_with_key_check`

Caches a value in Redis with a key,
if the key already exists a new key is generated by appending a UUID4.

```python
def cache_redis_with_key_check(key: str, value: str,
                               millis: int) -> str:
    """
    :param key: Key of the value to be stored
    :param value: Value to be stored
    :param millis: Expiration time in milliseconds
    :return: Key used to store the value in Redis
    """
```

### `redis_delete`

Deletes the value of a key in Redis. Returns the key value

```python
def redis_delete(key: str) -> Optional[Any]:
    """
    :param key: Key of the value to be deleted
    :return: The value of the key that was deleted.
    """
```

### `redis_incr`

Checks if the key is used, and if it is to be replaced
Increments the value of a key in Redis by the specified amount. Expires the key by days.

```python
def redis_incr(key: str, amount: int = 1,
               replace: Optional[bool]=True,
               days: Optional[int]=None) -> bool:
    """
    :param key: Key of the value to be incremented
    :param amount: Amount to increment the value
        (default 1)
    :param replace: If True, replace the value
      if the key already exists.
                    If False, return False
      if the key already exists.
                    Default is True.
    :param days: Expiration time in days,
      if None it will never expire
    :return: True if the value was successfully set,
      False if the key already exists and `replace`
      is False
    """
```

### `redis_decr`

Checks if the key is used, and if it is to be replaced
Decrements the value of a key in Redis by the specified amount. Expires the key by days.

```python
def redis_decr(key: str, amount: int = 1,
               replace: Optional[bool]=True,
               days: Optional[int]=None) -> bool:
    """
    :param key: Key of the value to be incremented
    :param amount: Amount to increment the value
        (default 1)
    :param replace: If True, replace the value
      if the key already exists.
                    If False, return False
      if the key already exists.
                    Default is True.
    :param days: Expiration time in days,
      if None it will never expire
    :return: True if the value was successfully set,
      False if the key already exists and `replace`
      is False
    """
```

### `redis_perxpire`

Set a time-to-live (TTL) for a key based on a Unix timestamp. 
If the timestamp is None and the persist flag is True, remove the TTL, making the key persistent.
Returns True if the TTL was set or removed, False if the key does not exist.

```python
def redis_perxpire(key: str, timestamp: Union[int, None] = None,
                 persist: bool = False) -> bool:
    """    
    :param key: The key to set the TTL for.
    :param timestamp: The Unix timestamp for the TTL.
        If None and persist is True, remove the TTL.
    :param persist: A flag indicating whether to remove the TTL
        (if True) or set it (if False).
    :return: True if the TTL was set or removed,
        False if the key does not exist.
    """
```

### `redis_get_keys`

Get a list of keys in Redis that match a given pattern. Can delete the keys found

```python
def redis_get_keys(pattern: str = None,
                   delete_keys: bool = False) -> List[str]:
    """
    Args:
        pattern (str, optional): Pattern for matching keys.
        Defaults to None.
        delete_keys (bool, optional): Whether to delete all keys.
        Defaults to False.
    Returns:
        List[str]: List of key strings.
    """
```

### `redis_rename`

Rename a key in Redis. If the new key already exists, the operation will fail
unless the overwrite parameter is set to True. Can delete the old key.

```python
def redis_rename(key: str, new_key: str, overwrite: bool = False,
                 delete_old: bool = False) -> List[bool]:
    """
    Args:
        key (str): The existing key to rename.
        new_key (str): The new name for the key.
        overwrite (bool, optional): If True,
            overwrite the new key if it already exists.
            Defaults to False.
        delete_old (bool, optional): If True,
            delete the old key after it has been renamed.
            Defaults to False.

    Returns:
        List[bool]: List[1] True if the key was successfully renamed,
            False otherwise.
                    List[2] True if the key was successfully deleted,
            False otherwise.
    """
```
