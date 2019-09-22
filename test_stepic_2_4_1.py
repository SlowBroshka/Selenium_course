from functools import partial

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import os
import math

DRIVER = 'Drivers\\chromedriver.exe'

def main(link):
    browser = webdriver.Chrome(DRIVER)
    browser.get(link)
    #browser.implicitly_wait(5)

    try:
        browser.find_element_by_id("button")


    except Exception as ex:
        print('!!!Error!!!')
        print(ex)
    finally:
        print('Close Browser')
        time.sleep(2)
        browser.close()
        browser.quit()


if __name__ == '__main__':
    LINK = 'http://suninjuly.github.io/cats.html'
    main(LINK)

