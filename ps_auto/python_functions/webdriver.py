"""
This script holds methods pertaining to Selenium webdriver functionality.
"""

from datetime import datetime
import selenium.webdriver.support.ui as ui
from allure import attachment_type, attach
from selenium.webdriver.common.keys import Keys

# from selenium.common.exceptions import \
#     NoSuchElementException, TimeoutException
# from variables import screenshot_location


# Maximum number of seconds to wait for an element to be present
timeout = 30


def screenshot_to_report(context):
    """
    Description:
        Takes a screenshot of the browser and saves it to a file named
        'error-<timestamp>.png'.
        Note that this method is to be used via Jenkins. The commented method
        of the same name below should be used when run from local machine.
    """
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = "error-{}.png".format(now)
    attach(
        context.browser.get_screenshot_as_png(),
        name=filename,
        attachment_type=attachment_type.PNG,
    )


def locate_element_by(context, by_loc, locator):
    """
    Description:
        Attempts to find the element(s) using the given method and element
        locator.
    Args:
        by_loc (str): Selenium method to use. Ex. 'find_element_by_xpath'. Must
            be one of methods defined in
            https://selenium-python.readthedocs.io/locating-elements.html
        locator (str): Unique identifier to find desired element
    Returns:
        First matching element or all matching elements, depending on the
        method used.
    Raises:
        AssertionError if element not found.
    """
    try:
        wait = ui.WebDriverWait(context.browser, timeout)
        element = wait.until(lambda browser: getattr(browser, by_loc)(locator))
        context.exc = None
        return element
    except Exception as e:
        context.exc = e
        print("\nElement '{}' not found".format(locator))
        screenshot_to_report(context)


def by_xpath(context, locator):
    """
    Description:
        Finds the first element with the given XPath.
    Args:
        locator (str): HTML XPath to search for
    Returns:
        First element that is found with the given XPath
    """
    return locate_element_by(context, "find_element_by_xpath", locator)


def by_id(context, locator):
    """
    Description:
        Finds the first element with the given ID.
    Args:
        locator (str): HTML ID to search for
    Returns:
        First element that is found with the given ID
    """
    return locate_element_by(context, "find_element_by_id", locator)


def by_element(context, locator):
    """
    Description:
        Finds the first match of the given element.
    Args:
        locator (str): Element to search for
    Returns:
        First element that matches
    """
    return locate_element_by(context, "find_element", locator)


def by_text(context, locator):
    """
    Description:
        Finds the first element with the given link text.
    Args:
        locator (str): Link text to search for
    Returns:
        First element that is found with the given link text
    """
    return locate_element_by(context, "find_element_by_link_text", locator)


def by_part_text(context, locator):
    """
    Description:
        Finds the first HTML link element whose text includes the given string.
    Args:
        locator (str): Link substring to search for
    Returns:
        First element that is found with the given substring in the linked text
    """
    return locate_element_by(
        context, "find_element_by_partial_link_text", locator
    )


def by_tag(context, locator):
    """
    Description:
        Finds the first element with the given HTML tag.
    Args:
        locator (str): HTML tag to search for, ex. 'h1'
    Returns:
        First element that is found with the given tag
    """
    return locate_element_by(context, "find_element_by_tag_name", locator)


def by_name(context, locator):
    """
    Description:
        Finds the first element with the given HTML name.
    Args:
        locator (str): HTML name to search for
    Returns:
        First element that is found with the given name
    """
    return locate_element_by(context, "find_element_by_name", locator)


def by_css(context, locator):
    """
    Description:
        Finds the first element with the given HTML CSS selector.
    Args:
        locator (str): HTML CSS selector to search for
    Returns:
        First element that is found with the given CSS selector
    """
    return locate_element_by(context, "find_element_by_css_selector", locator)


def by_class(context, locator):
    """
    Description:
        Finds the first element with the given HTML class name.
    Args:
        locator (str): HTML class name to search for
    Returns:
        First element that is found with the given class name
    """
    return locate_element_by(context, "find_element_by_class_name", locator)


def all_by_id(context, locator):
    """
    Description:
        Finds all elements with the given ID.
    Args:
        locator (str): HTML ID to search for
    Returns:
        All elements that are found with the given ID
    """
    return locate_element_by(context, "find_elements_by_id", locator)


def all_by_xpath(context, locator):
    """
    Description:
        Finds all elements with the given XPath.
    Args:
        locator (str): HTML XPath to search for
    Returns:
        All elements that are found with the given XPath
    """
    return locate_element_by(context, "find_elements_by_xpath", locator)


def all_by_element(context, locator):
    """
    Description:
        Finds all matches of the given element.
    Args:
        locator (str): Element to search for
    Returns:
        All elements that match
    """
    return locate_element_by(context, "find_elements", locator)


def all_by_text(context, locator):
    """
    Description:
        Finds all elements with the given link text.
    Args:
        locator (str): Link text to search for
    Returns:
        All elements that are found with the given link text
    """
    return locate_element_by(context, "find_elements_by_link_text", locator)


def all_by_part_text(context, locator):
    """
    Description:
        Finds all HTML link elements whose text includes the given string.
    Args:
        locator (str): Link substring to search for
    Returns:
        All elements that are found with the given substring in the linked text
    """
    return locate_element_by(
        context, "find_elements_by_partial_link_text", locator
    )


def all_by_tag(context, locator):
    """
    Description:
        Finds all elements with the given HTML tag.
    Args:
        locator (str): HTML tag to search for, ex. 'h1'
    Returns:
        All elements that are found with the given tag
    """
    return locate_element_by(context, "find_elements_by_tag_name", locator)


def all_by_name(context, locator):
    """
    Description:
        Finds all elements with the given HTML name.
    Args:
        locator (str): HTML name to search for
    Returns:
        All elements that are found with the given name
    """
    return locate_element_by(context, "find_elements_by_name", locator)


def all_by_css(context, locator):
    """
    Description:
        Finds all elements with the given HTML CSS selector.
    Args:
        locator (str): HTML CSS selector to search for
    Returns:
        All elements that are found with the given CSS selector
    """
    return locate_element_by(context, "find_elements_by_css_selector", locator)


def all_by_class(context, locator):
    """
    Description:
        Finds all elements with the given HTML class name.
    Args:
        locator (str): HTML class name to search for
    Returns:
        All elements that are found with the given class name
    """
    return locate_element_by(context, "find_elements_by_class_name", locator)


def scroll_to_top(context):
    """
    Description:
        Scroll to the top of the current page.
    """
    body = by_tag(context, "body")
    body.send_keys(Keys.CONTROL + Keys.HOME)
