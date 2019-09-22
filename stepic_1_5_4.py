import time
import math
from selenium.webdriver.common.by import By
from selenium import webdriver
DRIVER = 'Drivers\\chromedriver.exe'


LINK = 'http://suninjuly.github.io/find_xpath_form'

driver = webdriver.Chrome(DRIVER)
driver.get(LINK)

try:
    elms = driver.find_elements_by_tag_name('input')
    for elm in elms:
        elm.send_keys('My Answer')

    button = driver.find_element_by_xpath('html//button[text()=\'Отправить\']')
    button.click()

except Exception as exp:
    print("!!!!ERROR!!!!")
    print(exp)
    print("!!!!ERROR!!!!")
finally:
    time.sleep(5)
    driver.close()
    driver.quit()
