from selenium import webdriver
import time
import math

DRIVER = 'Drivers\\chromedriver.exe'


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


def find_x(page):
    span_tag = page.find_element_by_css_selector('#input_value')
    return span_tag.text


def find_func_input(page):
    return page.find_element_by_css_selector('input.form-control')


def click_checkbox(page):
    page.find_element_by_css_selector('input[type=checkbox][required]').click()


def click_radiobutton(page):
    page.find_element_by_css_selector('input[type=radio]#robotsRule').click()


def click_send(page):
    button = page.find_element_by_css_selector("button.btn")
    button.click()


def main(link):
    browser = webdriver.Chrome(DRIVER)
    browser.get(link)

    try:

        x = find_x(browser)
        find_func_input(browser).send_keys(calc(x))
        click_checkbox(browser)
        click_radiobutton(browser)
        click_send(browser)

    except Exception as ex:
        print('!!!Error!!!')
        print(ex)
        time.sleep(5)
    finally:
        print('Close Browser')
        browser.close()
        browser.quit()


if __name__ == '__main__':
    LINK = 'http://suninjuly.github.io/math.html'
    main(LINK)

