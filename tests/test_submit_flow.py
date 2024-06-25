from classes.SubmitFlow import SubmitFlow
import pytest

@pytest.mark.submit
def test_submit_flow(driver):
    submit_flow = SubmitFlow(driver)
    submit_flow.open()
    submit_flow.select_restaurant("22 Spring St","22 Spring St, Spring St, Manhattan")