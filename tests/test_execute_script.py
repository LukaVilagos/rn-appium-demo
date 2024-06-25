import pytest

@pytest.mark.general
def test_execute_script(driver):
   driver.execute_script('mobile: longClickGesture', {'x': 764, 'y': 295, 'duration': 1000})
   driver.execute_script('mobile: swipeGesture', {"left": 800, "top": 700, "width": 200, "height": 200, "direction": "right", "percent": 0.75})
   print(driver.execute_script('mobile: batteryInfo'))
   print(driver.execute_script('mobile: getPermissions'))
   print(driver.execute_script('mobile: getNotifications'))
   print(driver.execute_script('mobile: listSms'))
   print(driver.context)