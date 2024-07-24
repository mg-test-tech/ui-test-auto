import os
import time
import datetime
from datetime import datetime
import pdftotext
import sh
import tabula


# ------------------------------------------------------------------------------
def get_screenshot_always(context):
    now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    context.browser.get_screenshot_as_file(screenshot_location +
                                           'screenshot-' + now + '.png')


def sleeping(secs):
    time.sleep(secs)
    pass


def navigate_to_url(context, URL):
    context.browser.get(URL)


def login(context, username, password):
    username_field = by_id(context, username_locator)
    username_field.clear()
    username_field.send_keys(username)
    password_field = by_id(context, password_locator)
    password_field.clear()
    password_field.send_keys(password)
    sign_in_button = by_name(context, login_button_locator)
    sign_in_button.click()


def rename_pdf():
    file_name = str(sh.ls('-L', './data/in/'))
    file_name = file_name.replace("'", "")
    file_name = file_name.replace('"', '')
    file_name = file_name.replace("\n", "")
    new_file_name = sh.mv(dir_in + file_name, dir_in + 'work_on_file.pdf')
    return new_file_name


def clean_dir(directory):
    os.system('rm -rf ' + directory + '* || true')


def clean_file():
    with open(dir_out + 'one_file_tables.txt', 'r') as file:
        filedata = file.read()
    filedata = filedata.replace(',', ' ')
    filedata = filedata.replace('"', '')
    filedata = filedata.replace('""', '')
    filedata = filedata.replace('""', '')
    filedata = filedata.replace('  ', ' ')
    with open(dir_out + 'one_file_tables.txt', 'w') as file:
        file.write(filedata)
    file.close()


# convert pdf to txt, separate pages
def pages(dir_in, dir_out, input_file):
    name_list = []
    with open(input_file, 'rb') as f_in:
        pdf = pdftotext.PDF(f_in)
        total_pages = len(pdf)
        for x in range(1, len(pdf) + 1):
            page = 'page_' + str(x) + '.txt'
            name_list.append(page)
    return name_list, total_pages


# convert pdf to txt, one file
def one_txt_file(dir_in, dir_out, input_file):
    out_file = dir_out + 'one_page.txt'
    with open(input_file, "rb") as f:
        pdf = pdftotext.PDF(f)
        with open(out_file, 'w') as f_out:
            for page in pdf:
                f_out.write(page)
    f.close()


# convert pdf tables to txt, one file
def one_tables_file(dir_in, dir_out, input_file):
    name_list, total_pages = pages(dir_in=dir_in, dir_out=dir_out,
                                   input_file=input_file)
    for i in range(total_pages):
        out_csv = dir_out + 'one_file_tables.txt'
        tabula.convert_into(input_file, out_csv, output_format='csv',
                            guess=False, pages='all')


def check_if_downloaded():
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


def rename_file(out_file):
    file_name = str(sh.ls('-L', './data/in/')).replace("'", "")
    file_name = file_name.replace("\n", "")
    new_file_name = sh.mv(dir_in + file_name, dir_in + out_file)
    return new_file_name


def kill_chrome():
    os.system('killall chromedriver chrome')

