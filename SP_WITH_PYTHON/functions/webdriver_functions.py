from datetime import datetime
import selenium.webdriver.support.ui as ui
from allure import attachment_type, attach
from selenium.webdriver.common.by import By
from variables import screenshot_location

DEFAULT_TIMEOUT = 10

def screenshot_to_report(context):
    """
    Description:
        Takes a screenshot of the browser and saves it to a file named
        'error-<timestamp>.png'.
        Note that this method is to be used via Jenkins. The commented method
        of the same name below should be used when run from local machine.
    """
    now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    filename = "error-{}.png".format(now)
    attach(context.browser.get_screenshot_as_png(), name=filename,
           attachment_type=attachment_type.PNG)

# def screenshot_on_error(context, screenshot_location):
#     """
#     Take screenshot of the browser and saves it to file named
#     'error-<timestamp>.png'.
#     Note: use this function with execution from local machine
#     """
#     now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
#     context.browser.get_screenshot_as_file(f'{screenshot_location}screenshot-{now}.png')

def locate_element_by(context, by_loc, locator, timeout=DEFAULT_TIMEOUT):
    """
    Description:
        Attempts to find the element(s) using the given method and element
        locator.
    Args:
        context (obj): Selenium context
        by_loc (str): Selenium method to use. Ex. 'By.XPATH'. Must
            be one of methods defined in
            https://selenium-python.readthedocs.io/locating-elements.html
        locator (str): Unique identifier to find desired element
        timeout (int): Maximum number of seconds to wait for element
    Returns:
        First matching element or all matching elements, depending on the
        method used.
    Raises:
        AssertionError if element not found.
    """
    try:
        wait = ui.WebDriverWait(context.browser, timeout)
        element = wait.until(lambda browser: browser.find_element(by_loc, locator))
        context.exc = None
        return element
    except Exception as e:
        context.exc = e
        print("\nElement '{}' not found".format(locator))
        screenshot_to_report(context)

def locate_elements_by(context, by_loc, locator, timeout=DEFAULT_TIMEOUT):
    """
    Description:
        Attempts to find all elements using the given method and element
        locator.
    Args:
        context (obj): Selenium context
        by_loc (str): Selenium method to use. Ex. 'By.XPATH'. Must
            be one of methods defined in
            https://selenium-python.readthedocs.io/locating-elements.html
        locator (str): Unique identifier to find desired element
        timeout (int): Maximum number of seconds to wait for element
    Returns:
        First matching element or all matching elements, depending on the
        method used.
    Raises:
        AssertionError if element not found.
    """
    try:
        wait = ui.WebDriverWait(context.browser, timeout)
        element = wait.until(lambda browser: browser.find_elements(by_loc, locator))
        context.exc = None
        return element
    except Exception as e:
        context.exc = e
        print("\nElements '{}' not found".format(locator))
        screenshot_to_report(context)

#--SINGLE ELEMENT------------------------------------------------------------------------------------------------------
def by_xpath(context, locator, timeout=DEFAULT_TIMEOUT):
    """
    Description:
        Finds the first element with the given XPath.
    Args:
        locator (str): HTML XPath to search for
        timeout (int): Maximum number of seconds to wait for element
    Returns:
        First element that is found with the given XPath
    """
    return locate_element_by(
        context, 'By.XPATH', locator, timeout=timeout
    )


def by_id(context, locator, timeout=DEFAULT_TIMEOUT):
    """
    Description:
        Finds the first element with the given ID.
    Args:
        context (obj): Selenium context
        locator (str): HTML ID to search for
        timeout (int): Maximum number of seconds to wait for element
    Returns:
        First element that is found with the given ID
    """
    return locate_element_by(
        context, 'By.ID', locator, timeout=timeout
    )


def by_text(context, locator, timeout=DEFAULT_TIMEOUT):
    """
    Description:
        Finds the first element with the given link text.
    Args:
        locator (str): Link text to search for
    Returns:
        First element that is found with the given link text
    """
    return locate_element_by(
        context, 'By.LINK_TEXT', locator, timeout=timeout
    )


def by_part_text(context, locator, timeout=DEFAULT_TIMEOUT):
    """
    Description:
        Finds the first HTML link element whose text includes the given string.
    Args:
        locator (str): Link substring to search for
    Returns:
        First element that is found with the given substring in the linked text
    """
    return locate_element_by(
        context, 'By.PARTIAL_LINK_TEXT', locator, timeout=timeout
    )


def by_tag(context, locator, timeout=DEFAULT_TIMEOUT):
    """
    Description:
        Finds the first element with the given HTML tag.
    Args:
        locator (str): HTML tag to search for, ex. 'h1'
    Returns:
        First element that is found with the given tag
    """
    return locate_element_by(
        context, 'By.TAG_NAME', locator, timeout=timeout
    )


def by_name(context, locator, timeout=DEFAULT_TIMEOUT):
    """
    Description:
        Finds the first element with the given HTML name.
    Args:
        locator (str): HTML name to search for
    Returns:
        First element that is found with the given name
    """
    return locate_element_by(
        context, 'By.NAME', locator, timeout=timeout
    )


def by_css(context, locator, timeout=DEFAULT_TIMEOUT):
    """
    Description:
        Finds the first element with the given HTML CSS selector.
    Args:
        locator (str): HTML CSS selector to search for
    Returns:
        First element that is found with the given CSS selector
    """
    return locate_element_by(
        context, 'By.CSS_SELECTOR', locator, timeout=timeout
    )


def by_class(context, locator, timeout=DEFAULT_TIMEOUT):
    """
    Description:
        Finds the first element with the given HTML class name.
    Args:
        locator (str): HTML class name to search for
    Returns:
        First element that is found with the given class name
    """
    return locate_element_by(
        context, 'By.CLASS_NAME', locator, timeout=timeout
    )

#--ALL ELEMENT--------------------------------------------------------------------------------------------------------
def all_by_xpath(context, locator, timeout=DEFAULT_TIMEOUT):
    """
    Description:
        Finds all element with the given XPath.
    Args:
        locator (str): HTML XPath to search for
        timeout (int): Maximum number of seconds to wait for element
    Returns:
        all elements that is found with the given XPath
    """
    return locate_elements_by(
        context, 'By.XPATH', locator, timeout=timeout
    )


def all_by_id(context, locator, timeout=DEFAULT_TIMEOUT):
    """
    Description:
        Finds all element with the given ID.
    Args:
        context (obj): Selenium context
        locator (str): HTML ID to search for
        timeout (int): Maximum number of seconds to wait for element
    Returns:
        all element that is found with the given ID
    """
    return locate_elements_by(
        context, 'By.ID', locator, timeout=timeout
    )


def all_by_text(context, locator, timeout=DEFAULT_TIMEOUT):
    """
    Description:
        Finds all element with the given link text.
    Args:
        locator (str): Link text to search for
    Returns:
        all element that is found with the given link text
    """
    return locate_elements_by(
        context, 'By.LINK_TEXT', locator, timeout=timeout
    )


def all_by_part_text(context, locator, timeout=DEFAULT_TIMEOUT):
    """
    Description:
        Finds all HTML link element whose text includes the given string.
    Args:
        locator (str): Link substring to search for
    Returns:
        all element that is found with the given substring in the linked text
    """
    return locate_elements_by(
        context, 'By.PARTIAL_LINK_TEXT', locator, timeout=timeout
    )


def all_by_tag(context, locator, timeout=DEFAULT_TIMEOUT):
    """
    Description:
        Finds all element with the given HTML tag.
    Args:
        locator (str): HTML tag to search for, ex. 'h1'
    Returns:
        all element that is found with the given tag
    """
    return locate_elements_by(
        context, 'By.TAG_NAME', locator, timeout=timeout
    )


def all_by_name(context, locator, timeout=DEFAULT_TIMEOUT):
    """
    Description:
        Finds all element with the given HTML name.
    Args:
        locator (str): HTML name to search for
    Returns:
        all element that is found with the given name
    """
    return locate_elements_by(
        context, 'By.NAME', locator, timeout=timeout
    )


def all_by_css(context, locator, timeout=DEFAULT_TIMEOUT):
    """
    Description:
        Finds all element with the given HTML CSS selector.
    Args:
        locator (str): HTML CSS selector to search for
    Returns:
        all element that is found with the given CSS selector
    """
    return locate_elements_by(
        context, 'By.CSS_SELECTOR', locator, timeout=timeout
    )


def all_by_class(context, locator, timeout=DEFAULT_TIMEOUT):
    """
    Description:
        Finds all element with the given HTML class name.
    Args:
        locator (str): HTML class name to search for
    Returns:
        all element that is found with the given class name
    """
    return locate_elements_by(
        context, 'By.CLASS_NAME', locator, timeout=timeout
    )