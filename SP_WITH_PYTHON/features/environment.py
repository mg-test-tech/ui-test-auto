import sys
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains

from functions.common_functions import kill_chrome
from variables import chrome_location

options = Options()
options.add_argument("--headless=new")
chrome_service = Service(executable_path=chrome_location)


def before_all(context):
    context.browser = webdriver.Chrome(service=chrome_service, options=options)
    context.browser.implicitly_wait(20)
    context.browser.maximize_window()


def after_all(context):
    time.sleep(5)
    context.browser.quit()
    # kill_chrome()
