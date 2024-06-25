from appium.webdriver.common.appiumby import AppiumBy
import elements

class SubmitFlow:
    def __init__(self, driver) -> None:
        self.driver = driver
        
    def get_open_button(self):
        return self.driver.find_element(AppiumBy.XPATH, elements.SUBMIT_FLOW_OPEN_BUTTON)

    def get_search_restaurants_input(self):
        return self.driver.find_element(AppiumBy.XPATH, elements.SEARCH_RESTAURANTS_INPUT)
    
    def get_upload_confirmation_button(self):
        return self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, elements.UPLOAD_SCREENSHOT_BUTTON)
    
    def open(self) -> None:
        self.get_open_button().click()
        self.driver.implicitly_wait(1)
        
    def select_restaurant(self, query, restaurant_id):
        self.get_search_restaurants_input().send_keys(query)
        self.driver.implicitly_wait(0.5)
        restaurant_card = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, restaurant_id)
        restaurant_card.click()
        
    def upload_screenshot(self, image_id):
        self.get_upload_confirmation_button().click()
        self.driver.implicitly_wait(3)
        
        if self.driver.capabilities['platformName'] == "Android":
            image_to_select = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, image_id)
            
        image_to_select.click()