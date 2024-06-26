from PIL import Image
import io
import pytest

@pytest.mark.general
def test_save_screenshot(driver):
    image = Image.open(io.BytesIO(driver.get_screenshot_as_png()))
    image.save("screenshot.png")