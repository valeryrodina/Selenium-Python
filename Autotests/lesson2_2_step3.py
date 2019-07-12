from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math

def calc(x,z):
  return str(int(x)+int(z))

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_id("num1")
x = x_element.text

z_element = browser.find_element_by_id("num2")
z = z_element.text

y = calc(x,z)

select = Select(browser.find_element_by_id("dropdown"))
select.select_by_value(y)

button = browser.find_element_by_css_selector("button.btn")
button.click()





