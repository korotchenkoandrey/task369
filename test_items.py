from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_item_add_to_basket(browser):
    browser.get(link)
    element1 = browser.find_element_by_css_selector("form button.btn-add-to-basket")
    assert element1.text, "Element hasn't been found"
