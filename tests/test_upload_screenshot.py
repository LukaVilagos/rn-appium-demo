from classes.SubmitFlow import SubmitFlow
import pytest

def test_upload_screenshot(driver):
    submit_flow = SubmitFlow(driver)
    submit_flow.upload_screenshot("Photo taken on Jun 25, 2024, 1:12:34 PM")