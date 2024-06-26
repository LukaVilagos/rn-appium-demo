import os
import pytest
import logging
import datetime
from appium import webdriver
from appium.options.android import UiAutomator2Options

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

EXECUTOR = 'http://127.0.0.1:4723'
ANDROID_APP_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'android')

apk_files = [f for f in os.listdir(ANDROID_APP_DIR) if f.endswith('.apk')]
assert len(apk_files) == 1, 'App directory can only contain one app file.'
ANDROID_APP_PATH = os.path.join(ANDROID_APP_DIR, apk_files.pop(0))

options = UiAutomator2Options()
options.app = ANDROID_APP_PATH
options.app_package = 'com.resx.test'
options.app_activity = 'com.resx.test.MainActivity'
options.platform_name = 'Android'
options.device_name = 'emulator-5554'
options.automation_name = 'UiAutomator2'
options.no_reset = True

@pytest.fixture(scope="module")
def driver():
    driver_instance = webdriver.Remote(EXECUTOR, options=options)
    yield driver_instance
    driver_instance.quit()
    
def pytest_configure(config):
    reports_dir = "reports"
    if not os.path.exists(reports_dir):
        os.makedirs(reports_dir)

    now = datetime.datetime.now()
    report_filename = now.strftime("%Y-%m-%d_%H-%M-%S_report.html")

    report_path = os.path.join(reports_dir, report_filename)
    config.option.htmlpath = report_path