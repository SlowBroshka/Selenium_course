from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import os

DRIVER = 'Drivers\\chromedriver.exe'




def fill_req(page):
    input_elms = page.find_elements_by_css_selector('input[required]')
    for input in input_elms:
        type = input.get_attribute('type')
        if type == 'text':
            input.send_keys(input.get_attribute('name'))
        elif type == 'file':
            curr_dir = os.path.abspath(os.path.dirname(__file__))
            f_path = os.path.join(curr_dir, 'temp.txt')
            print(os.path.abspath(__file__))
            print(os.path.abspath(os.path.dirname(__file__)))
            input.send_keys(f_path)


def input_val(page, val):
    field = page.find_element_by_id('answer')
    field.send_keys(val)


def scroll_page(page, elm):
    page.execute_script("return arguments[0].scrollIntoView(true);", elm)


def set_checkboxes(page):
    checkbox_1 = page.find_element_by_css_selector('input[type=checkbox]')
    scroll_page(page, checkbox_1)
    checkbox_1.click()
    checkbox_2 = page.find_element_by_css_selector('input[type=\'radio\'][value=\'robots\']')
    scroll_page(page, checkbox_2)
    checkbox_2.click()


def send_form(page):
    button = page.find_element_by_css_selector('button[type=\'submit\']')
    scroll_page(page, button)
    button.click()


def main(link):
    browser = webdriver.Chrome(DRIVER)
    browser.get(link)
    time.sleep(1)

    try:
        fill_req(browser)
        send_form(browser)
        time.sleep(1)

    except Exception as ex:
        print('!!!Error!!!')
        print(ex)
    finally:
        print('Close Browser')
        time.sleep(2)
        browser.close()
        browser.quit()


if __name__ == '__main__':
    LINK = "http://suninjuly.github.io/file_input.html"
    main(LINK)

