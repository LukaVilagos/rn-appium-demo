import time

def test_app_inspect():
    try:
        print("Appium session is running. Press Ctrl+C to quit.")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Exiting...")