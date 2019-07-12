from selenium import webdriver
import os

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)

input1 = browser.find_element_by_css_selector('.form-group > [name="firstname"]')
input1.send_keys("Lera")

input2 = browser.find_element_by_css_selector('.form-group > [name="lastname"]')
input2.send_keys("Rodina")

input3 = browser.find_element_by_css_selector('.form-group > [name="email"]')
input3.send_keys("gdgdffd@dfgdfgdg.com")

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')

input4 = browser.find_element_by_id("file")
input4.send_keys(file_path)

button = browser.find_element_by_css_selector("button.btn")
button.click()




