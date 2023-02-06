import os
import sys
import traceback

from selenium import webdriver
from fake_useragent import UserAgent
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ip_utils import useful_proxies_gen


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


def driver_wait(driver: WebDriver, time: int, xpath: str) -> None:
    """
    Wait for an element to be clickable

    :param driver: The webdriver instance
    :type driver: WebDriver
    :param time: Time to wait
    :type time: int
    :param xpath: xpath of the element
    :type xpath: str
    """
    try:
        WebDriverWait(driver, time).until(
            EC.element_to_be_clickable((By.XPATH, xpath)))
    except Exception:
        print("Element not found.")
        print(traceback.format_exc())
        driver.quit()
        sys.exit()


def click_element(driver: WebDriver,
                  time: int, xpath: str) -> None:
    """
    Click on an element

    :param driver: The webdriver instance
    :type driver: WebDriver
    :param time: Time to wait
    :type time: int
    :param xpath: xpath of the element
    :type xpath: str
    """
    driver_wait(driver, time, xpath)
    driver.find_element(By.XPATH, xpath).click()


def type_into_element(driver: WebDriver, time: int,
                      xpath: str, text: str) -> None:
    """
    Type text into an element

    :param driver: The webdriver instance
    :type driver: WebDriver
    :param time: Time to wait
    :type time: int
    :param xpath: xpath of the element
    :type xpath: str
    :param text: Text to type
    :type text: str
    """
    driver_wait(driver, time, xpath)
    element = driver.find_element(By.XPATH, xpath)
    element.clear()
    element.send_keys(text)


file_name = os.path.splitext(os.path.basename(os.path.abspath(__file__)))[0]
dir_name = os.path.basename(os.path.dirname(os.path.abspath(__file__)))
if __name__ == "__main__" or __name__ == f"{dir_name}.{file_name}":
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
