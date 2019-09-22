from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

DRIVER = 'Drivers\\chromedriver.exe'


def calc(x):
    return math.log(abs(12 * math.sin(int(x))))


def get_X(page):
    return page.find_element_by_id('input_value').text

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
        x = get_X(browser)
        calc_val = str(calc(x))
        input_val(browser, calc_val)
        set_checkboxes(browser)
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
    LINK = "http://SunInJuly.github.io/execute_script.html"
    main(LINK)

