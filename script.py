import time
from selenium.webdriver.common.by import By
from selenium import webdriver
DRIVER = 'Drivers\\chromedriver.exe'


LINK = 'http://suninjuly.github.io/simple_form_find_task.html'

driver = webdriver.Chrome(DRIVER)
driver.get(LINK)

try:
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

    time.sleep(5)
except Exception as exp:
    print("!!!!ERROR!!!!")
    print(exp)
    print("!!!!ERROR!!!!")
finally:
    time.sleep(5)
    driver.close()
    driver.quit()

# search_box = driver.find_element_by_name('q')
# search_box.send_keys('ChromeDriver')
# search_box.submit()
#
#

