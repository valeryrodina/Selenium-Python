from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_id("input_value")
x = x_element.text

y = calc(x)

button = browser.find_element_by_css_selector("button.btn")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

input1 = browser.find_element_by_id("answer")
input1.send_keys(y)

chkbx = browser.find_element_by_id("robotCheckbox")
chkbx.click()

rdbtn = browser.find_element_by_css_selector("[value='robots']")
rdbtn.click()

button.click()





