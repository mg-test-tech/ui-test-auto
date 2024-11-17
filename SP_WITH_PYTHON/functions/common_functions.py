import os
import time
from lib2to3.fixes.fix_input import context

from selenium.webdriver import ActionChains, Keys

from variables import screenshot_location, dir_in

def sleeping(secs):
    '''
    Description: pause script execution for given number os seconds
    :param secs: int
    '''
    time.sleep(secs)


def clean_dir(directory):
    '''
    Description: remove files from given directory
    :param directory: str, path to directory
    '''
    os.system('rm -rf ' + directory + '* || true')


def kill_chrome():
    '''
    Description: kill chrome and chromedriver processes
    '''
    os.system('killall chromedriver chrome')


def check_if_downloaded():
    '''
    Description: check dir_in directory for file downloaded
    '''
    file_list = os.listdir(dir_in)
    print(len(file_list))
    while len(file_list) == 0:
        print('no files')
        file_list = os.listdir(dir_in)
        sleeping(5)
        if len(file_list) == 1:
            print('file is downloaded')
            break
        sleeping(5)


