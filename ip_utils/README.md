# ip_utils

A module to check the current ip and get a free proxy for small requests.

An IP address, or Internet Protocol address, is a unique numerical identifier assigned to every device connected to the internet. It allows devices to communicate with each other over the internet by sending and receiving data packets.

IP addresses come in two versions: IPv4 and IPv6. IPv4 addresses are 32-bit numbers expressed in decimal format, and are made up of four sets of numbers between 0 and 255, separated by periods. For example, "192.168.0.1" is a typical IPv4 address. IPv6 addresses are 128-bit numbers expressed in hexadecimal format, and are made up of eight sets of four hexadecimal digits, separated by colons. For example, "2001:0db8:85a3:0000:0000:8a2e:0370:7334" is a typical IPv6 address.

IP addresses are used by internet protocols to route data packets from one device to another over the internet. Each device connected to the internet is assigned a unique IP address, which allows it to be identified and located by other devices on the internet. IP addresses are assigned to devices by Internet Service Providers (ISPs) or other organizations that manage networks.

In addition to identifying devices on the internet, IP addresses can also be used to determine the location of a device. Geolocation services can use IP address information to determine the approximate location of a device, which can be useful for a variety of purposes, such as targeted advertising or content delivery. However, it's important to note that IP address-based geolocation is not always accurate, and can be affected by a variety of factors, such as the use of VPNs or proxies.

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
