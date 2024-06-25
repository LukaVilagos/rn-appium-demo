import pytest

@pytest.mark.failed
def test_get(driver):
    driver.get("https://www.google.com/")