from appium.webdriver.common.appiumby import AppiumBy
from elements.submit_elements import SubmitElements
import pytest

def test_find_element(driver):
    new_york_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, SubmitElements.NEW_YORK_CITY_SELECT_BUTTON.value)
    assert new_york_button
    print(new_york_button.is_displayed())
    new_york_button.is_enabled()
    new_york_button.screenshot('foo.png')