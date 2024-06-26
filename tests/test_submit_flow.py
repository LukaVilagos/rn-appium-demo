from classes.SubmitFlow import SubmitFlow
import pytest

@pytest.mark.submit
def test_submit_flow(driver):
    submit_flow = SubmitFlow(driver)
    submit_flow.open()
    submit_flow.select_city('new york')
    submit_flow.select_restaurant("22 Spring St")
    submit_flow.select_location('indoor')
    submit_flow.input_location_details('location details')
    submit_flow.click_when_button()