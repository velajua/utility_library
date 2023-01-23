from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from ip_utils import useful_proxies_gen


def getDriver(*mods: str) -> webdriver.Chrome:
    '''
    *mods: String
    userAgent: adds a random user agent to the driver
    incognito: adds incognito mode to the driver
    proxy: creates proxy connection through the driver
    proxy={PROXY:PORT} - overwrites the default proxy, requires proxy
    maximize: adds maximize mode to the driver
    '''
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

def driver_wait(driver: webdriver.Chrome, time: int, xpath: str) -> None:
    WebDriverWait(driver, time).until(EC.element_to_be_clickable((By.XPATH, xpath)))
