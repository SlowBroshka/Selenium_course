from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

DRIVER = 'Drivers\\chromedriver.exe'


def calc(x1, x2):
    return int(x1) + int(x2)


def get_nums(page):
    num1 = page.find_element_by_id('num1').text
    num2 = page.find_element_by_id('num2').text
    return num1, num2


def click_sum(page, sum):
    select = Select(page.find_element_by_tag_name('select'))
    select.select_by_visible_text(sum)


def send_form(page):
    page.find_element_by_css_selector('button[type=\'submit\']').click()


def main(link):
    browser = webdriver.Chrome(DRIVER)
    browser.get(link)
    time.sleep(1)

    try:
        n1, n2 = get_nums(browser)
        sum = str(calc(n1, n2))
        click_sum(browser, sum)
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
    LINK = 'http://suninjuly.github.io/selects2.html'
    main(LINK)

