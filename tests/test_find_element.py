from appium.webdriver.common.appiumby import AppiumBy
import elements
import pytest

@pytest.mark.general
def test_find_element(driver):
    new_york_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, elements.NEW_YORK_BUTTON)
    assert new_york_button
    print(new_york_button.is_displayed())
    new_york_button.screenshot('foo.png')