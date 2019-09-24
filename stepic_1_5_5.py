from selenium import webdriver
import time

DRIVER = 'Drivers\\chromedriver.exe'


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


def main(link):
    browser = webdriver.Chrome(DRIVER)    #DRIVER
    browser.get(link)

    try:
        fill_required_fields(browser)
        click_register(browser)
        time.sleep(2)

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text

    except Exception as ex:
        print('!!!Error!!!')
        print(ex)
    finally:
        print('Close Browser')
        browser.quit()


if __name__ == '__main__':
    LINK = 'http://suninjuly.github.io/registration1.html'
    main(LINK)

