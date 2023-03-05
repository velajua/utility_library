# selenium_utils

A module to create a Chrome webdriver with specified options and perform actions on web elements.
This module uses a webdriver manager to install the chromedriver. Thus, no chrome driver is needed in the folder.

Selenium is a popular open-source framework for automating web browsers. It provides a set of tools and APIs to automate web browsers and perform various tasks, such as testing web applications, web scraping, and web automation.

Selenium is primarily used to automate testing of web applications. It allows developers and testers to write automated test scripts in various programming languages, such as Python, Java, C#, and Ruby. These test scripts can then be executed on different web browsers, such as Chrome, Firefox, Safari, and Internet Explorer, to test the functionality of the web application under different conditions.

Selenium provides a set of APIs to interact with web elements, such as buttons, links, text fields, and dropdowns. It can simulate user actions such as clicking, typing, and scrolling. Selenium also provides the ability to capture screenshots, manage cookies and sessions, and handle pop-ups and alerts.

Selenium can be used to perform web scraping, where it can extract data from websites by navigating to web pages, extracting data from HTML elements, and saving the data in a structured format, such as CSV or JSON.

Overall, Selenium is a powerful tool for web automation and testing, and is widely used in the software development industry. It provides a flexible and reliable way to automate repetitive tasks and test the functionality of web applications.

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

### `find_element_data`

Find and return data about HTML elements on a webpage using Selenium WebDriver.

```python
def find_element_data(driver: WebDriver, contains_text: Union[str, List[str]] = '',
                      contains_class: Union[str, List[str]] = '',
                      contains_id: Union[str, List[str]] = '',
                      contains_src: Union[str, List[str]] = '',
                      contains_style: Union[str, List[str]] = '',
                      contains_name: Union[str, List[str]] = '',
                      contains_title: Union[str, List[str]] = '',
                      contains_alt: Union[str, List[str]] = '',
                      return_element: bool = False, tag_name: str = '*',
                      return_xpath: bool = False, time: int = 30) -> Union[
                          Dict[str, Union[str, Dict[str, str]]],
                          List[selenium.webdriver.remote.webelement.WebElement],
                          str, List]:
    """
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
```

### `cookie_manager`

Function to manage cookies in a Selenium WebDriver session.

```python
def cookie_manager(driver: WebDriver, path: str = 'cookies.pkl',
                   get_: bool = False) -> None:
    """
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
```
