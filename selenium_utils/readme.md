# selenium_utils

A module to create a Chrome webdriver with specified options and perform actions on web elements.

## Installation

To install the required packages, run:

pip install -r requirements.txt


## Usage

### `getDriver`

This function creates and returns a Chrome webdriver with specified options.

```python
def getDriver(*mods: str) -> webdriver.Chrome:
    """
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
```

### `driver_wait`

Waits for an element to be clickable.

```
def driver_wait(driver: WebDriver, time: int,
                xpath: str) -> Union[None, bool]:
    """
    :param driver: The webdriver instance
    :type driver: WebDriver
    :param time: Time to wait
    :type time: int
    :param xpath: xpath of the element
    :type xpath: str
    :return: True after the element has been found.
    :rtype: Union[None, bool]
    """
```

### `click_element`

Clicks on an element.

```python
def click_element(driver: WebDriver,
                  time: int, xpath: str) -> bool:
    """
    :param driver: The webdriver instance
    :type driver: WebDriver
    :param time: Time to wait
    :type time: int
    :param xpath: xpath of the element
    :type xpath: str
    :return: True after the element has been clicked.
    :rtype: bool
    """
```

### `type_or_get_text`

Types or gets text into/from an element.

```python
def type_or_get_text(driver: WebDriver, time: int,
                     xpath: str, text: str = None,
                     action: str = None) -> Union[bool, str]:
    """
    :param driver: The webdriver instance
    :type driver: WebDriver
    :param time: Time to wait
    :type time: int
    :param xpath: xpath of the element
    :type xpath: str
    :param text: Text to type
    :type text: str
    :param action: "type" to type text or "get" to get text
    :type action: str
    :return: True after typing text or the text of the element.
    :rtype: Union[bool, str]
    """
```

### `page_interaction`

Perform various actions on the current page of the given webdriver.

```python
def page_interaction(driver: WebDriver, action: str,
                     route: str = None) -> Union[bool, str]:
    """
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
```
