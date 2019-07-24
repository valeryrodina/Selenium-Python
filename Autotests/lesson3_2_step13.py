import unittest
from selenium import webdriver
import time


class TestAbs(unittest.TestCase):

    def test_first(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration1.html")
        input1 = browser.find_element_by_css_selector(".first_block .first_class .first")
        input1.send_keys("Lera")
        input2 = browser.find_element_by_css_selector(".first_block .second_class .second")
        input2.send_keys("Rodina")
        input3 = browser.find_element_by_css_selector(".first_block .third_class .third")
        input3.send_keys("test@gmail.com")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Поздравляем! Вы успешно зарегистировались!", welcome_text, "Registration failed")

    def test_second(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration2.html")
        input1 = browser.find_element_by_css_selector(".first_block .first_class .first")
        input1.send_keys("Lera")
        input2 = browser.find_element_by_css_selector(".first_block .second_class .second")
        input2.send_keys("Rodina")
        input3 = browser.find_element_by_css_selector(".first_block .third_class .third")
        input3.send_keys("test@gmail.com")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Поздравляем! Вы успешно зарегистировались!", welcome_text, "Registration failed")


if __name__ == "__main__":
    unittest.main()
