# ip_utils

A module to check the current ip and get a free proxy for small requests.

## Installation

To install the required packages, run:

pip install -r requirements.txt


## Usage

### `my_ip`

This function retrieves the current IP address of the device by making a request to 'http://icanhazip.com'
It can also use a proxy to make the request if provided. Returns a string containing the set of IPs found or
None in case of errors.

```python
def my_ip(proxies: dict = None) -> Union[str, None]:
    """    
    :param proxies: A dictionary containing the proxy settings
        to be used for the request. Default is None
    :type proxies: dict
    :return: a string containing the set of IPs found
        or None in case of errors.
    :rtype: Union[str, None]
    """
```

### `useful_proxies_gen`

 A generator function that yields useful free proxies.

```python
def useful_proxies_gen(type_: str='dict') -> Iterator[
        Union[str, Dict[str, str]]]:
    """
    Parameters:
    type_ (str): The type of output desired, either 'dict'
    or 'data'. Defaults to 'dict'.
    Yields:
    Union[str, Dict[str, str]]: A proxy in the format
    specified by the type_ parameter.
    """
```
    
    
