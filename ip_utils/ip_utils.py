import os
import re
import sys
import requests
import traceback

from typing import Iterator, Union, Dict, List
from bs4 import BeautifulSoup


def my_ip(proxies: dict = None) -> Union[str, None]:
    """
    This function retrieves the current IP address of the
    device by making a request to 'http://icanhazip.com'
    It can also use a proxy to make the request if provided.
    Returns a string containing the set of IPs found or
    None in case of errors.
    
    :param proxies: A dictionary containing the proxy settings
        to be used for the request. Default is None
    :type proxies: dict
    :return: a string containing the set of IPs found
        or None in case of errors.
    :rtype: Union[str, None]
    """
    try:
        url = 'http://icanhazip.com'
        r = requests.get(url=url, proxies=proxies)
    except Exception:
        # print the traceback in case of an exception
        print(traceback.format_exc())
        return None

    if r.status_code != 200:
        print(f'request status: {r.status_code}')
        return None

    # using regular expression to find IP addresses in the response
    regex = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
    ip = regex.findall(r.text)
    ip = [i for i in ip if ip and not i.startswith('0')]
    # format the result
    ans = f'set of IPs found are {set(ip)}'
    return ans
  
  
def useful_proxies_gen(type_: str='dict') -> Iterator[
        Union[str, Dict[str, str]]]:
    """
    A generator function that yields useful proxies.

    Parameters:
    type_ (str): The type of output desired, either 'dict'
    or 'data'. Defaults to 'dict'.

    Yields:
    Union[str, Dict[str, str]]: A proxy in the format
    specified by the type_ parameter.
    """
    def get_free_proxies() -> List[str]:
        """
        A helper function that scrapes a website for free proxies.
        Returns:
        List[str]: A list of proxy addresses in the format IP:PORT
        """
        url = "https://free-proxy-list.net/"
        soup = BeautifulSoup(requests.get(url).content, "lxml")
        r = soup.find('textarea', {'class': 'form-control'})

        regex = re.compile(
            r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\:\d{2,5})')
        ip = regex.findall(r.text)
        proxies = [i for i in ip if ip and not i.startswith('0')]
        return proxies
    
    def get_session(proxies: str) -> requests.Session:
        """
        A helper function that creates a requests session
        with a specific proxy.
        
        Parameters:
        proxies (str): A proxy address in the format IP:PORT

        Returns:
        requests.Session: A session object with the specified
        proxy set.
        """
        session = requests.Session()
        session.proxies = {"http": proxies, "https": proxies}
        return session

    for i in get_free_proxies():
        s = get_session(i)
        try:
            ip = s.get("http://icanhazip.com", timeout=1.5).text.strip()
            if any(y in ip for y in ['Not authenticated', '<!DOCTYPE']):
                continue
            print("Request page with IP:", ip)
            if type_ == 'data':
                yield i
            elif type_ == 'dict':
                yield {'http': f'http://{i}',
                       'https': f'https://{i}'}
        except Exception:
            continue


file_name = os.path.splitext(os.path.basename(os.path.abspath(__file__)))[0]
dir_name = os.path.basename(os.path.dirname(os.path.abspath(__file__)))
if __name__ == "__main__" or __name__ == f"{dir_name}.{file_name}":
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
