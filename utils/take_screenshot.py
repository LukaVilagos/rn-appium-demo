from PIL import Image
import io
import datetime
import os

def take_screenshot(driver):
    screenshots_dir = "static/screenshots"
    if not os.path.exists(screenshots_dir):
        os.makedirs(screenshots_dir)
        
    now = datetime.datetime.now()
    screenshot_filename = now.strftime("%Y-%m-%d_%H-%M-%S_screenshot.png")
    
    screenshot_path = os.path.join(screenshots_dir, screenshot_filename)
    
    image = Image.open(io.BytesIO(driver.get_screenshot_as_png()))
    image.save(screenshot_path)