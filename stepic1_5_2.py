import time
import math
from selenium.webdriver.common.by import By
from selenium import webdriver
DRIVER = 'Drivers\\chromedriver.exe'


LINK = 'http://suninjuly.github.io/find_link_text'

driver = webdriver.Chrome(DRIVER)
driver.get(LINK)

try:
    text = str(math.ceil(math.pow(math.pi, math.e)*10000))
    print(text)
    link = driver.find_element_by_partial_link_text(text)
    link.click()

    input1 = driver.find_element_by_tag_name('input')
    input1.send_keys("IGOR")

    input2 = driver.find_element_by_name('last_name')
    input2.send_keys('NIkoLaev')

    input3 = driver.find_element_by_class_name('city')
    input3.send_keys('LA')

    input4 = driver.find_element_by_id('country')
    input4.send_keys('CCCR')

    button = driver.find_element_by_css_selector('.btn')
    button.click()

except Exception as exp:
    print("!!!!ERROR!!!!")
    print(exp)
    print("!!!!ERROR!!!!")
finally:
    time.sleep(5)
    driver.close()
    driver.quit()
