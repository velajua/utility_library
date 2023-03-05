import os
import sys
import pickle

import selenium

from selenium import webdriver
from fake_useragent import UserAgent
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.ip_utils import useful_proxies_gen

from typing import Union, Dict, List


def getDriver(*mods: str) -> webdriver.Chrome:
    """
    This function creates and returns a Chrome webdriver
    with specified options.

    *mods: str
    userAgent: adds a random user agent to the driver
    incognito: adds incognito mode to the driver
    proxy: creates proxy connection through the driver
    proxy={PROXY:PORT} - overwrites the default proxy, requires proxy
    maximize: adds maximize mode to the driver
    headless: run the browser in headless mode
    
    :return: webdriver with the *mods specified.
    :rtype: webdriver.Chrome
    """
    chrome_options = webdriver.ChromeOptions()
    capabilities = DesiredCapabilities.CHROME

    prefs = {"profile.managed_default_content_settings.images": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1024, 768")
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("--disable-notifications")

    if 'userAgent' in mods:
        chrome_options.add_argument(
            f"user-agent={UserAgent().random}")
    if 'incognito' in mods:
        chrome_options.add_argument('--incognito')
    if 'proxy' in mods:
        proxy_ = [x.split('=')[-1] for x in mods if 'proxy=' in x]
        if not proxy_:
            proxy_ = next(useful_proxies_gen(type_='data'))
        else:
            proxy_ = proxy_[0]
        chrome_options.add_argument(f'--proxy-server=http://{proxy_}')
    if 'headless' in mods:
        chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(
        ChromeDriverManager().install(),
        options=chrome_options,
        desired_capabilities=capabilities)
    if 'maximize' in mods:
        driver.maximize_window()
    return driver


def driver_wait(driver: WebDriver, time: int,
                xpath: str, clickable=True) -> Union[None, bool]:
    """
    Wait for an element to be clickable

    :param driver: The webdriver instance
    :type driver: WebDriver
    :param time: Time to wait
    :type time: int
    :param xpath: xpath of the element
    :type xpath: str
    :return: True after the element has been found.
    :rtype: Union[None, bool]
    """
    try:
        WebDriverWait(driver, time).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
            if clickable
            else EC.presence_of_element_located((By.XPATH, xpath)))
        return True
    except Exception:
        print(f"Element {xpath} not found.")
        # driver.quit()
        # sys.exit()


def click_element(driver: WebDriver,
                  time: int, xpath: str) -> bool:
    """
    Click on an element

    :param driver: The webdriver instance
    :type driver: WebDriver
    :param time: Time to wait
    :type time: int
    :param xpath: xpath of the element
    :type xpath: str
    :return: True after the element has been clicked.
    :rtype: bool
    """
    driver_wait(driver, time, xpath)
    driver.find_element(By.XPATH, xpath).click()
    return True


def type_or_get_text(driver: WebDriver, time: int,
                     xpath: str, text: str = None,
                     action: str = None) -> Union[bool, str]:
    """
    Type or get text into/from an element

    :param driver: The webdriver instance
    :type driver: WebDriver
    :param time: Time to wait
    :type time: int
    :param xpath: xpath of the element
    :type xpath: str
    :param text: Text to type
    :type text: str
    :param action: Action to do. One of: 'type' and 'get'
    :type action: str
    """
    driver_wait(driver, time, xpath)
    element = driver.find_element(By.XPATH, xpath)
    if action == 'type':
        element.clear()
        element.send_keys(text)
        return True
    elif action == 'get':
        return element.text
    else:
        return False


def page_interaction(driver: WebDriver, action: str,
                     route: str = None) -> Union[bool, str]:
    """
    Perform various actions on the current page of the
    given webdriver.

    :param driver: The webdriver instance
    :type driver: WebDriver
    :param action: The action to perform on the current page.
        One of: "back", "forward", "refresh", "screenshot", "source".
    :type action: str
    :param route: The file path to save the result to.
        Required for actions "screenshot" and "source".
    :type route: str, optional
    :return: The page source or screenshot file, or None
        if the action was "back", "forward", or "refresh".
    :rtype: Union[bool, str]
    """
    if action == "back":
        driver.back()
        return True
    elif action == "forward":
        driver.forward()
        return True
    elif action == "refresh":
        driver.refresh()
        return True
    elif action == "screenshot":
        if route:
            driver.get_screenshot_as_file(route)
            return route
        return driver.get_screenshot_as_base64()
    elif action == "source":
        if route:
            with open(route, "w") as f:
                f.write(driver.page_source)
            return route
        return driver.page_source
    else:
        return False


def find_element_data(driver, contains_text='', contains_class='',
                      contains_id='', contains_src='', contains_style='',
                      contains_name='', return_element=False,
                      return_xpath=False, time=30) -> Union[
                          Dict[str, Union[str, Dict[str, str]]],
                          List[selenium.webdriver.remote.webelement.WebElement],
                          str, List]:
    """
    Find and return data about HTML elements on a webpage using
    Selenium WebDriver.

    Args:
        driver: An instance of a Selenium WebDriver.
        contains_?: Optional ? that the element should contain.
        return_element: Optional flag to indicate whether to return the
            element(s) found or not. Default is False.
        return_xpath: Optional flag to indicate whether to return the XPath
            of the element(s) found or not. Default is False.

    Returns:
        If neither `return_element` nor `return_xpath` is True, a list of
            dictionaries with data about the element(s) found.
        Each dictionary has the keys 'tag_name', 'text', and the attributes
            of the element.
        If `return_element` is True and only one element is found,
            the element object is returned.
        If `return_element` is True and multiple elements are found,
            a list of element data objects is returned.
        If `return_xpath` is True and only one element is found,
            the XPath string is returned.
    """
    tags = [contains_text, contains_class, contains_id, contains_src,
            contains_style, contains_name]
    prefix = ['text()', '@class', '@id', '@src', '@style', '@name']
    
    xpath_ = f'''//*[{" and ".join([f"contains{k}"
        for k in [(prefix[i], j) for i, j in enumerate(tags) if j]]) }]'''
    [xpath_ := xpath_.replace(f"'{i}'", i) for i in prefix]
    driver_wait(driver, time, xpath_)
    elements_ = driver.find_elements(By.XPATH, xpath_)
    if return_xpath and len(elements_) == 1:
        return xpath_
    elif not elements_:
        return f'None found with xpath {xpath_}' 

    data_ =  [driver.execute_script(
        '''var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index)
 { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value };
 return items;''', e) | {'tag_name': e.tag_name, 'text': e.text} for e in elements_]
    data_ =  data_ if len(data_) > 1 else data_[0] if not return_element else elements_[0]
    return data_


def cookie_manager(driver: WebDriver, path: str = 'cookies.pkl',
                   get_: bool = False) -> None:
    """
    Function to manage cookies in a Selenium WebDriver session.

    Args:
        driver (WebDriver): A Selenium WebDriver instance.
        path (str, optional): The path to the file where the
            cookies are saved. Defaults to 'cookies.pkl'.
        get_ (bool, optional): If True, saves the cookies
            from the WebDriver session to the specified file. 
                              If False, loads the cookies
            from the specified file and adds them to the WebDriver session. 
                              Defaults to False.
    """
    if get_:
        pickle.dump(driver.get_cookies(), open(path, "wb"))
    else:
        cookies: List[dict] = pickle.load(open(path, "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)


file_name = os.path.splitext(os.path.basename(os.path.abspath(__file__)))[0]
dir_name = os.path.basename(os.path.dirname(os.path.abspath(__file__)))
if __name__ == "__main__" or __name__ == f"{dir_name}.{file_name}":
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
