import pytest

@pytest.mark.failed
def test_cookie(driver):
    driver.add_cookie({'name' : 'foo', 'value' : 'bar'})
    driver.get_cookie("foo")
    driver.delete_cookie("foo")