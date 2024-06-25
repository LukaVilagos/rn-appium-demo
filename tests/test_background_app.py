import pytest

@pytest.mark.general
def test_background_app(driver):
    driver.background_app(2)