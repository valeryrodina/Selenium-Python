from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

sunduk = browser.find_element_by_id("treasure")
sunduk_valuex = sunduk.get_attribute("valuex")

y = calc(sunduk_valuex)

input1 = browser.find_element_by_id("answer")
input1.send_keys(y)

chkbx = browser.find_element_by_id("robotCheckbox")
chkbx.click()

rdbtn = browser.find_element_by_css_selector("[value='robots']")
rdbtn.click()

button = browser.find_element_by_css_selector("button.btn")
button.click()





