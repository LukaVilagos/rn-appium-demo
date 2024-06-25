import pytest

@pytest.mark.failed
def test_shake(driver):
    driver.shake()