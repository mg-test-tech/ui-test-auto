from datetime import datetime
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By
from variables import screenshot_location

timeout = 10

def screenshot_on_error(context, screenshot_location):
    now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    context.browser.get_screenshot_as_file(f'{screenshot_location}screenshot-{now}.png')


def by_xpath(context, locator):
    try:
        wait = ui.WebDriverWait(context.browser, timeout)
        element = wait.until(lambda browser: browser.find_element(By.XPATH, locator))
        context.exc = None
        return element
    except Exception as e:
        context.exc = e
        print('\nElement {} not found'.format(locator))
        screenshot_on_error(context, screenshot_location)


def by_id(context, locator):
    try:
        wait = ui.WebDriverWait(context.browser, timeout)
        element = wait.until(lambda browser: browser.find_element(By.ID, locator))
        context.exc = None
        return element
    except Exception as e:
        context.exc = e
        print('\nElement {} not found'.format(locator))
        screenshot_on_error(context, screenshot_location)


def by_text(context, locator):
    try:
        wait = ui.WebDriverWait(context.browser, timeout)
        element = wait.until(lambda browser: browser.find_element(By.LINK_TEXT, locator))
        context.exc = None
        return element
    except Exception as e:
        context.exc = e
        print('\nElement {} not found'.format(locator))
        screenshot_on_error(context, screenshot_location)


def by_part_text(context, locator):
    try:
        wait = ui.WebDriverWait(context.browser, timeout)
        element = wait.until(lambda browser: browser.find_element(By.PARTIAL_LINK_TEXT, locator))
        context.exc = None
        return element
    except Exception as e:
        context.exc = e
        print('\nElement {} not found'.format(locator))
        screenshot_on_error(context, screenshot_location)


def by_tag(context, locator):
    try:
        wait = ui.WebDriverWait(context.browser, timeout)
        element = wait.until(lambda browser: browser.find_element(By.TAG_NAME, locator))
        context.exc = None
        return element
    except Exception as e:
        context.exc = e
        print('\nElement {} not found'.format(locator))
        screenshot_on_error(context, screenshot_location)


def by_name(context, locator):
    try:
        wait = ui.WebDriverWait(context.browser, timeout)
        element = wait.until(lambda browser: browser.find_element(By.NAME, locator))
        context.exc = None
        return element
    except Exception as e:
        context.exc = e
        print('\nElement {} not found'.format(locator))
        screenshot_on_error(context, screenshot_location)


def by_css(context, locator):
    try:
        wait = ui.WebDriverWait(context.browser, timeout)
        element = wait.until(lambda browser: browser.find_element(By.CSS_SELECTOR, locator))
        context.exc = None
        return element
    except Exception as e:
        context.exc = e
        print('\nElement {} not found'.format(locator))
        screenshot_on_error(context, screenshot_location)


def by_class(context, locator):
    try:
        wait = ui.WebDriverWait(context.browser, timeout)
        element = wait.until(lambda browser: browser.find_element(By.CLASS_NAME, locator))
        context.exc = None
        return element
    except Exception as e:
        context.exc = e
        print('\nElement {} not found'.format(locator))
        screenshot_on_error(context, screenshot_location)


# =============================================================================================
def all_by_id(context, locator):
    try:
        wait = ui.WebDriverWait(context.browser, timeout)
        element = wait.until(lambda browser: browser.find_elements(By.ID, locator))
        context.exc = None
        return element
    except Exception as e:
        context.exc = e
        print('\nElement {} not found'.format(locator))
        screenshot_on_error(context, screenshot_location)


def all_by_xpath(context, locator):
    try:
        wait = ui.WebDriverWait(context.browser, timeout)
        element = wait.until(lambda browser: browser.find_elements(By.XPATH, locator))
        context.exc = None
        return element
    except Exception as e:
        context.exc = e
        print('\nElement {} not found'.format(locator))
        screenshot_on_error(context, screenshot_location)


def all_by_text(context, locator):
    try:
        wait = ui.WebDriverWait(context.browser, timeout)
        element = wait.until(lambda browser: browser.find_elements(By.LINK_TEXT, locator))
        context.exc = None
        return element
    except Exception as e:
        context.exc = e
        print('\nElement {} not found'.format(locator))
        screenshot_on_error(context, screenshot_location)


def all_by_part_text(context, locator):
    try:
        wait = ui.WebDriverWait(context.browser, timeout)
        element = wait.until(lambda browser: browser.find_elements(By.PARTIAL_LINK_TEXT, locator))
        context.exc = None
        return element
    except Exception as e:
        context.exc = e
        print('\nElement {} not found'.format(locator))
        screenshot_on_error(context, screenshot_location)


def all_by_tag(context, locator):
    try:
        wait = ui.WebDriverWait(context.browser, timeout)
        element = wait.until(lambda browser: browser.find_elements(By.TAG_NAME, locator))
        context.exc = None
        return element
    except Exception as e:
        context.exc = e
        print('\nElement {} not found'.format(locator))
        screenshot_on_error(context, screenshot_location)


def all_by_name(context, locator):
    try:
        wait = ui.WebDriverWait(context.browser, timeout)
        element = wait.until(lambda browser: browser.find_elements(By.NAME, locator))
        context.exc = None
        return element
    except Exception as e:
        context.exc = e
        print('\nElement {} not found'.format(locator))
        screenshot_on_error(context, screenshot_location)


def all_by_css(context, locator):
    try:
        wait = ui.WebDriverWait(context.browser, timeout)
        element = wait.until(lambda browser: browser.find_elements(By.CSS_SELECTOR, locator))
        context.exc = None
        return element
    except Exception as e:
        context.exc = e
        print('\nElement {} not found'.format(locator))
        screenshot_on_error(context, screenshot_location)


def all_by_class(context, locator):
    try:
        wait = ui.WebDriverWait(context.browser, timeout)
        element = wait.until(lambda browser: browser.find_elements(By.CLASS_NAME, locator))
        context.exc = None
        return element
    except Exception as e:
        context.exc = e
        print('\nElement {} not found'.format(locator))
        screenshot_on_error(context, screenshot_location)
