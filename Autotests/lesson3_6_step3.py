from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time
import math


def calc():
    return str(math.log(int(time.time())))


@pytest.mark.parametrize('link', ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1",
                                  "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1",
                                  "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1",
                                  "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"])
def test_guest_should_see_login_link(link):
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    browser.get(link)

    input1 = browser.find_element_by_css_selector(".quiz-component .textarea")
    x = calc()
    input1.send_keys(x)

    button = browser.find_element_by_class_name("submit-submission")
    button.click()

    WebDriverWait(browser, 5).until(
     EC.visibility_of_element_located((By.CLASS_NAME, "correct_icon"))
    )

    optional_fdb = browser.find_element_by_class_name("smart-hints__hint")
    opt_fdb = optional_fdb.text
    assert opt_fdb == "Correct!", \
        "Wrong value: " + opt_fdb + " not Correct!"
    browser.quit()

