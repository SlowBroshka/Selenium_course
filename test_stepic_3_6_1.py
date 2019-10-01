import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import math


DRIVER = 'Drivers\\chromedriver.exe'


def calc_answer():
    return math.log(int(time.time()))


pages_list = [
    'https://stepik.org/lesson/236895/step/1',
    'https://stepik.org/lesson/236896/step/1',
    'https://stepik.org/lesson/236897/step/1',
    'https://stepik.org/lesson/236898/step/1',
    'https://stepik.org/lesson/236899/step/1',
    'https://stepik.org/lesson/236903/step/1',
    'https://stepik.org/lesson/236904/step/1',
    'https://stepik.org/lesson/236905/step/1'
]
expected_text = 'Correct!'


class TestMainClass:

    def setup_method(self):
        print('setup_method')
        self.browser = webdriver.Chrome(DRIVER)

    def teardown_method(self):
        print('teardown_method')
        self.browser.quit()


    @pytest.mark.parametrize("page", pages_list)
    def test_pages(self, page):
        print(calc_answer())
        print(page)
        solve_lesson(self.browser, page, calc_answer)


def solve_lesson(browser, link, answ_func):
    browser.get(link)

    WebDriverWait(browser, 10).until(
        (EC.element_to_be_clickable((By.TAG_NAME, 'textarea')))
    ).send_keys(str(answ_func()))

    WebDriverWait(browser, 10).until(
        (EC.text_to_be_present_in_element((By.TAG_NAME, 'button'), 'Отправить'))
    )
    browser.find_element_by_css_selector('.submit-submission').click()

    WebDriverWait(browser, 10).until(
        (EC.visibility_of_element_located((By.TAG_NAME, 'pre')))
    )
    searched_text = browser.find_element_by_tag_name('pre').text
    assert  searched_text == expected_text, 'Site: \"{}\" expected: \"{}\". Search: \"{}\"'\
                                            .format(link, expected_text, searched_text)
