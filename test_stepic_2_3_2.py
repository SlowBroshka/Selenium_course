from functools import partial

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import os
import math

DRIVER = 'Drivers\\chromedriver.exe'



def get_X(page):
    return page.find_element_by_id('input_value').text


def calc(x):
    return math.log(abs(12 * math.sin(int(x))))


def input_val(page, val):
    field = page.find_element_by_id('answer')
    field.send_keys(val)


def send_form(page):
    button = page.find_element_by_css_selector('button[type=\'submit\']')
    button.click()


def send_alert(page):
    confirm = page.switch_to.alert
    confirm.accept()


def go_trip(page):
    button = page.find_element_by_css_selector('button[type=\'submit\']')
    button.click()
    send_alert(page)


def main(link):
    browser = webdriver.Chrome(DRIVER)
    browser.get(link)
    time.sleep(1)

    try:
        go_trip(browser)
        input_val(browser, str(calc(get_X(browser))))
        send_form(browser)

    except Exception as ex:
        print('!!!Error!!!')
        print(ex)
    finally:
        print('Close Browser')
        time.sleep(2)
        browser.close()
        browser.quit()


if __name__ == '__main__':
    LINK = 'http://suninjuly.github.io/alert_accept.html'
    main(LINK)

