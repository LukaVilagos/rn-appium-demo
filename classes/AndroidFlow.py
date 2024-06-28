from elements.common_elements import CommonElements
from appium.webdriver.common.appiumby import AppiumBy

class AndroidFlow:
    def __init__(self, driver) -> None:
        self.driver = driver
        
    #region Getters
    
    def get_ok_button(self):
        return self.driver.find_element(AppiumBy.ID, CommonElements.ANDROID_OK_BUTTON.value)
    
    #endregion