# redis_utils

A module with Redis functions to store and retrieve values and objects.

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