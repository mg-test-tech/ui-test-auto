from sys import modules
from behave import *
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from functions.app_functions import navigate_to_url
from functions.common_functions import sleeping
from functions.webdriver_functions_old import by_xpath, by_class, by_css, by_name, by_text, by_id, by_tag, all_by_tag
from web_elements import modules_xpath, repertoire_module_xpath, ps_text_locator_tag

use_step_matcher("re")


@when("user navigates to (?P<URL>.+) user can see navigation bar and item (?P<navbar_item>.+)")
def navigate_to_landing(context, URL, navbar_item):
    """
    :type context: behave.runner.Context
    :type URL: str
    :type navbar_item: str
    """
    navigate_to_url(context, URL)
    element = by_xpath(context, modules_xpath)
    assert element.text == navbar_item


@step("user clicks on (?P<navbar_item>.+) and clicks on (?P<menu_item>.+) from dropdown menu")
def navigate_to_repertoire_management(context, navbar_item, menu_item):
    """
    :type context: behave.runner.Context
    :type navbar_item: str
    :type menu_item: str
    """
    by_xpath(context, modules_xpath).click()
    sleeping(2)
    rm_element = by_xpath(context, repertoire_module_xpath)
    assert rm_element.text == menu_item
    rm_element.click()


@step("user redirected to corresponding page (?P<app_page_url>.+)")
def validate_app_page_url(context, app_page_url):
    """
    :type context: behave.runner.Context
    :type app_page_url: str
    """
    address = context.browser.current_url
    assert address == app_page_url


@step("user scrolls down to Additional Features")
def scroll_down(context):
    """
    :type context: behave.runner.Context
    """
    for i in range(2):
        ActionChains(context.browser).key_down(Keys.PAGE_DOWN).perform()


@step("user clicks on Products Supported")
def click_on_products_supported(context):
    """
    :type context: behave.runner.Context
    """
    element = by_text(context, 'Products Supported')
    element.click()
    sleeping(1)


@then("user can see the text (?P<product_supported_text>.+)")
def assert_products_supported_text(context, product_supported_text):
    """
    :type context: behave.runner.Context
    :type product_supported_text: str
    """
    elements = all_by_tag(context, ps_text_locator_tag)
    element_text = elements[7].text
    assert element_text == product_supported_text
