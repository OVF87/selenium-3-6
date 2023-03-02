
from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_link_basket(browser):
    browser.get(link)
    time.sleep(10)
    btn = browser.find_elements(By.CSS_SELECTOR, "button[class*='basket']")
    assert len(btn) > 0

