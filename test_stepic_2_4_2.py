from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
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


def click_book_button(page):
    button = page.find_element_by_id('book')
    button.click()


def go_site(page):
    WebDriverWait(page, 20).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), "$100")
    )
    click_book_button(page)


def main(link):
    browser = webdriver.Chrome(DRIVER)
    browser.get(link)
    time.sleep(1)

    try:
        go_site(browser)
        time.sleep(1)

        input_val(browser, str(calc(get_X(browser))))
        send_form(browser)

        time.sleep(5)

    except Exception as ex:
        print('!!!Error!!!')
        print(ex)
    finally:
        print('Close Browser')
        time.sleep(2)
        browser.quit()


if __name__ == '__main__':
    LINK = 'http://suninjuly.github.io/explicit_wait2.html'
    main(LINK)

