from classes.SubmitFlow import SubmitFlow
import pytest

def test_submit_flow(driver):
    submit_flow = SubmitFlow(driver)
    submit_flow.open()
    submit_flow.select_city('new york')
    submit_flow.select_restaurant("22 Spring St")
    submit_flow.select_location('indoor')
    submit_flow.input_location_details('location details test')
    submit_flow.click_when_button()
    submit_flow.select_date("2024", "Jun", "28")
    submit_flow.select_time("PM", "9", "30")
    submit_flow.click_who_button()