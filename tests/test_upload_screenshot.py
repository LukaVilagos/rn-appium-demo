from classes.SubmitFlow import SubmitFlow
import pytest

@pytest.mark.screenshot
def test_submit_flow(driver):
    submit_flow = SubmitFlow(driver)
    submit_flow.upload_screenshot("Photo taken on Jun 25, 2024, 1:12:34 PM")