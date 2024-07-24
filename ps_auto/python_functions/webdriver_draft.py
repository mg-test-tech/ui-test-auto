from datetime import datetime
import selenium.webdriver.support.ui as ui
from variables import screenshot_location

timeout = 10

locator = ''
error_txt = '\nElement {} not found'.format(locator)


def screenshot_on_error(context, screenshot_location):
    now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    context.browser.get_screenshot_as_file(screenshot_location +
                                           'screenshot-' + now + '.png')


def by_xpath(context, locator):
    try:
        wait = ui.WebDriverWait(context.browser, timeout)
        element = wait.until(
            lambda browser: browser.find_element_by_xpath(locator))
        context.exc = None
        return element
    except Exception as e:
        context.exc = e
        print(error_txt)
        screenshot_on_error(context, screenshot_location)


def by_id(context, locator):
    try:
        wait = ui.WebDriverWait(context.browser, timeout)
        element = wait.until(
            lambda browser: browser.find_element_by_id(locator))
        context.exc = None
        return element
    except Exception as e:
        context.exc = e
        print(error_txt)
        screenshot_on_error(context, screenshot_location)


def by_element(context, locator):
    try:
        wait = ui.WebDriverWait(context.browser, timeout)
        element = wait.until(lambda browser: browser.find_element(locator))
        context.exc = None
        return element
    except Exception as e:
        context.exc = e
        print(error_txt)
        screenshot_on_error(context, screenshot_location)


def by_text(context, locator):
    try:
        wait = ui.WebDriverWait(context.browser, timeout)
        element = wait.until(
            lambda browser: browser.find_element_by_link_text(locator))
        context.exc = None
        return element
    except Exception as e:
        context.exc = e
        print(error_txt)
        screenshot_on_error(context, screenshot_location)


def by_part_text(context, locator):
    try:
        wait = ui.WebDriverWait(context.browser, timeout)
        element = wait.until(
            lambda browser: browser.find_element_by_partial_link_text(locator))
        context.exc = None
        return element
    except Exception as e:
        context.exc = e
        print(error_txt)
        screenshot_on_error(context, screenshot_location)


def by_tag(context, locator):
    try:
        wait = ui.WebDriverWait(context.browser, timeout)
        element = wait.until(
            lambda browser: browser.find_element_by_tag_name(locator))
        context.exc = None
        return element
    except Exception as e:
        context.exc = e
        print(error_txt)
        screenshot_on_error(context, screenshot_location)


def by_name(context, locator):
    try:
        wait = ui.WebDriverWait(context.browser, timeout)
        element = wait.until(
            lambda browser: browser.find_element_by_name(locator))
        context.exc = None
        return element
    except Exception as e:
        context.exc = e
        print(error_txt)
        screenshot_on_error(context, screenshot_location)


def by_css(context, locator):
    try:
        wait = ui.WebDriverWait(context.browser, timeout)
        element = wait.until(
            lambda browser: browser.find_element_by_css_selector(locator))
        context.exc = None
        return element
    except Exception as e:
        context.exc = e
        print(error_txt)
        screenshot_on_error(context, screenshot_location)


def by_class(context, locator):
    try:
        wait = ui.WebDriverWait(context.browser, timeout)
        element = wait.until(
            lambda browser: browser.find_element_by_class_name(locator))
        context.exc = None
        return element
    except Exception as e:
        context.exc = e
        print(error_txt)
        screenshot_on_error(context, screenshot_location)


# =============================================================================================
def all_by_id(context, locator):
    try:
        wait = ui.WebDriverWait(context.browser, timeout)
        element = wait.until(
            lambda browser: browser.find_elements_by_id(locator))
        context.exc = None
        return element
    except Exception as e:
        context.exc = e
        print(error_txt)
        screenshot_on_error(context, screenshot_location)


def all_by_xpath(context, locator):
    try:
        wait = ui.WebDriverWait(context.browser, timeout)
        element = wait.until(
            lambda browser: browser.find_elements_by_xpath(locator))
        context.exc = None
        return element
    except Exception as e:
        context.exc = e
        print(error_txt)
        screenshot_on_error(context, screenshot_location)


def all_by_element(context, locator):
    try:
        wait = ui.WebDriverWait(context.browser, timeout)
        element = wait.until(lambda browser: browser.find_elements(locator))
        context.exc = None
        return element
    except Exception as e:
        context.exc = e
        print(error_txt)
        screenshot_on_error(context, screenshot_location)


def all_by_text(context, locator):
    try:
        wait = ui.WebDriverWait(context.browser, timeout)
        element = wait.until(
            lambda browser: browser.find_elements_by_link_text(locator))
        context.exc = None
        return element
    except Exception as e:
        context.exc = e
        print(error_txt)
        screenshot_on_error(context, screenshot_location)


def all_by_part_text(context, locator):
    try:
        wait = ui.WebDriverWait(context.browser, timeout)
        element = wait.until(
            lambda browser: browser.find_elements_by_partial_link_text(
                locator))
        context.exc = None
        return element
    except Exception as e:
        context.exc = e
        print(error_txt)
        screenshot_on_error(context, screenshot_location)


def all_by_tag(context, locator):
    try:
        wait = ui.WebDriverWait(context.browser, timeout)
        element = wait.until(
            lambda browser: browser.find_elements_by_tag_name(locator))
        context.exc = None
        return element
    except Exception as e:
        context.exc = e
        print(error_txt)
        screenshot_on_error(context, screenshot_location)


def all_by_name(context, locator):
    try:
        wait = ui.WebDriverWait(context.browser, timeout)
        element = wait.until(
            lambda browser: browser.find_elements_by_name(locator))
        context.exc = None
        return element
    except Exception as e:
        context.exc = e
        print(error_txt)
        screenshot_on_error(context, screenshot_location)


def all_by_css(context, locator):
    try:
        wait = ui.WebDriverWait(context.browser, timeout)
        element = wait.until(
            lambda browser: browser.find_elements_by_css_selector(locator))
        context.exc = None
        return element
    except Exception as e:
        context.exc = e
        print(error_txt)
        screenshot_on_error(context, screenshot_location)


def all_by_class(context, locator):
    try:
        wait = ui.WebDriverWait(context.browser, timeout)
        element = wait.until(
            lambda browser: browser.find_elements_by_class_name(locator))
        context.exc = None
        return element
    except Exception as e:
        context.exc = e
        print(error_txt)
        screenshot_on_error(context, screenshot_location)
