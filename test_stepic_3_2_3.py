import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

DRIVER = 'Drivers\\chromedriver.exe'

test_expected_text = "Congratulations! You have successfully registered!"


def fill_required_fields(page):
    first = page.find_element_by_css_selector('.first_block input.first')
    first.send_keys('Name')

    second = page.find_element_by_css_selector('.first_block input.second')
    second.send_keys('Surname')

    third = page.find_element_by_css_selector('.first_block input.third')
    third.send_keys('third@email.com')


def click_register(page):
    button = page.find_element_by_css_selector("button.btn")
    button.click()


class TestMainClass:

    def setup_method(self):
        print('\nstart browser')
        self.browser = webdriver.Chrome(DRIVER)

    def teardown_method(self):
        print('\nquit browser')
        self.browser.quit()

    def test_reg_form1(self):
        LINK = 'http://suninjuly.github.io/registration1.html'
        self.browser.get(LINK)
        fill_required_fields(self.browser)
        click_register(self.browser)
        time.sleep(2)
        welcome_text_elt = self.browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        assert welcome_text == test_expected_text, "Reg test 1 fail actual: {} expected: {}".format(welcome_text, test_expected_text)

    def test_reg_form2(self):
        LINK = 'http://suninjuly.github.io/registration2.html'
        self.browser.get(LINK)
        with pytest.raises(NoSuchElementException):
            fill_required_fields(self.browser)
            pytest.fail("Не должно быть кнопки Отправить")
