from appium.webdriver.common.appiumby import AppiumBy
import elementos
from elements.submit_elements import SubmitElements
from elements.common_elements import CommonElements
from elements.navigation_elements import NavigationElements
from typing import Literal
from utils.element_exists import element_exists
from utils.take_screenshot import take_screenshot
import time
import logging

logger = logging.getLogger(__name__)

class SubmitFlow:
    def __init__(self, driver) -> None:
        self.driver = driver
        
    #region Getters
    
    #region general
    
    def get_heading(self):
        return self.driver.find_element(AppiumBy.XPATH, SubmitElements.HEADING.value)
    
    def get_progress_bar(self):
        return self.driver.find_element(AppiumBy.XPATH, SubmitElements.PROGRESS_BAR.value)
    
    def get_open_button(self):
        return self.driver.find_element(AppiumBy.XPATH, NavigationElements.SUBMIT_FLOW_NAV_BUTTON.value)
    
    def get_go_back_button(self):
        return self.driver.find_element(AppiumBy.XPATH, SubmitElements.GO_BACK_BUTTON.value)
    
    #endregion
    
    #region 1st screen
    
    def get_screen_one_subheading(self):
        return self.driver.find_element(AppiumBy.XPATH, SubmitElements.SCREEN_ONE_SUBHEADING.value)
    
    def get_search_restaurants_input(self):
        return self.driver.find_element(AppiumBy.CLASS_NAME, SubmitElements.SEARCH_RESTAURANTS_INPUT.value)
    
    def get_restaurants_search_top_result(self):
        return self.driver.find_element(AppiumBy.XPATH, SubmitElements.SEARCH_RESTAURANTS_TOP_RESULT.value)
    
    def get_indoor_button(self):
        return self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, SubmitElements.INDOOR_BUTTON.value)
    
    def get_outdoor_button(self):
        return self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, SubmitElements.OUTDOOR_BUTTON.value)
    
    def get_details_input_empty(self):
        return self.driver.find_element(AppiumBy.XPATH, SubmitElements.DETAILS_INPUT_EMPTY.value)
    
    def get_when_button(self):
        return self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, SubmitElements.WHEN_BUTTON.value)
    
    # navigation to menu buttons
    
    def get_change_city_new_york_button(self):
        return self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, SubmitElements.CHANGE_CITY_MENU_NEW_YORK_BUTTON.value)

    def get_change_city_miami_button(self):
        return self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, SubmitElements.CHANGE_CITY_MENU_MIAMI_BUTTON.value)
    
    def get_change_city_menu_arrow(self):
        return self.driver.find_element(AppiumBy.XPATH, SubmitElements.CHANGE_CITY_MENU_ARROW.value)
    
    # select buttons
    
    def get_new_york_city_select_button(self):
        return self.driver.find_element(AppiumBy.XPATH, SubmitElements.NEW_YORK_CITY_SELECT_BUTTON.value)
    
    def get_miami_city_select_button(self):
        return self.driver.find_element(AppiumBy.XPATH, SubmitElements.MIAMI_CITY_SELECT_BUTTON.value)
        
    
    #endregion
    
    #region 2nd screen
    
    def get_screen_two_subheading(self):
        return self.driver.find_element(AppiumBy.XPATH, SubmitElements.SCREEN_TWO_SUBHEADING.value)
    
    def get_select_date_input_empty(self):
        return self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, SubmitElements.SELECT_DATE_INPUT_EMPTY.value)
    
    #endregion
    
    #region 4th screen
    
    def get_upload_confirmation_button(self):
        return self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, elementos.UPLOAD_SCREENSHOT_BUTTON)
    
    #endregion
    
    #endregion
    
    #region Methods
    
    #region general
    
    def open(self) -> None:
        self.get_open_button().click()
        time.sleep(1)
        
        logger.info("Verifying 'Submit Flow Screen' is present")
        assert self.get_heading()
        assert self.get_progress_bar()
        
        logger.info("Verifying 'Submit Flow Screen 1' is present")
        assert self.get_screen_one_subheading()
        take_screenshot(self.driver)
        
    #endregion
    
    #region 1st screen
        
    def select_restaurant(self, query: str):
        self.get_search_restaurants_input().send_keys(query)
        time.sleep(1)
        self.get_restaurants_search_top_result().click()
        
        logger.info("Verifying 'When Button' is not enabled")
        assert not self.get_when_button().is_enabled()
        
    def select_city(self, city: Literal["new york", "miami"]):
        match city:
            case "new york":
                if not element_exists(self.get_change_city_new_york_button):
                    self.get_change_city_menu_arrow().click()
                    time.sleep(1)
                    self.get_new_york_city_select_button().click()
            case "miami":
                if not element_exists(self.get_change_city_miami_button):
                    self.get_change_city_menu_arrow().click()
                    time.sleep(1)
                    self.get_miami_city_select_button().click()
                    
        time.sleep(1)
        
    def select_location(self, location: Literal["indoor", "outdoor"]):
        match location:
            case "indoor":
                self.get_indoor_button().click()
            case "outdoor":
                self.get_outdoor_button().click()
        
        logger.info("Verifying 'When Button' is enabled")
        assert self.get_when_button().is_enabled()
        time.sleep(1)
                
    def input_location_details(self, details: str):
        self.get_details_input_empty().send_keys(details)
        
        logger.info("Verifying 'When Button' is not enabled")
        assert self.get_when_button().is_enabled()
        time.sleep(1)
        
    def click_when_button(self):
        logger.info("Verifying 'When Button' is not enabled")
        assert self.get_when_button().is_enabled()
        take_screenshot(self.driver)
        
        self.get_when_button().click()
        time.sleep(1)
        
        logger.info("Verifying 'Submit Flow Screen 2' is present")
        assert self.get_screen_two_subheading()
        
    #endregion
        
    #region 2nd screen
        
    def select_date(self, desired_year: str, desired_month: str, desired_day: str):
        self.get_select_date_input_empty().click()
        
        if not self.driver.find_element(AppiumBy.XPATH, f'''//android.widget.EditText[@resource-id="android:id/numberpicker_input" and @text="{desired_month}"]'''):
            self.driver.find_element(AppiumBy.XPATH, f'''//android.widget.Button[@text="{desired_month}"]''').click()
            
        if not self.driver.find_element(AppiumBy.XPATH, f'''//android.widget.EditText[@resource-id="android:id/numberpicker_input" and @text="{desired_day}"]'''):
            self.driver.find_element(AppiumBy.XPATH, f'''//android.widget.Button[@text="{desired_day}"]''').click()
            
        if not self.driver.find_element(AppiumBy.XPATH, f'''//android.widget.EditText[@resource-id="android:id/numberpicker_input" and @text="{desired_year}"]'''):
            self.driver.find_element(AppiumBy.XPATH, f'''//android.widget.Button[@text="{desired_year}"]''').click()
            
        CommonElements.ANDROID_OK_BUTTON.click()
        
    def select_time(self, desired_period: str, desired_hour: str, desired_minute: str):
        self.get_select_date_input_empty().click()
        
        if not self.driver.find_element(AppiumBy.XPATH, f'''//android.widget.EditText[@resource-id="android:id/numberpicker_input" and @text="{desired_hour}"]'''):
            self.driver.find_element(AppiumBy.XPATH, f'''//android.widget.Button[@text="{desired_hour}"]''').click()
            
        if not self.driver.find_element(AppiumBy.XPATH, f'''//android.widget.EditText[@resource-id="android:id/numberpicker_input" and @text="{desired_minute}"]'''):
            self.driver.find_element(AppiumBy.XPATH, f'''//android.widget.Button[@text="{desired_minute}"]''').click()
            
        if not self.driver.find_element(AppiumBy.XPATH, f'''//android.widget.EditText[@resource-id="android:id/numberpicker_input" and @text="{desired_period}"]'''):
            self.driver.find_element(AppiumBy.XPATH, f'''//android.widget.Button[@text="{desired_period}"]''').click()
            
        CommonElements.ANDROID_OK_BUTTON.click()
     
    #endregion
       
    #region 4th screen
        
    def upload_screenshot(self, image_id: str):
        self.get_upload_confirmation_button().click()
        self.driver.implicitly_wait(3)
        
        if self.driver.capabilities['platformName'] == "Android":
            image_to_select = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, image_id)
            
        image_to_select.click()
    
    #endregion
        
    #endregion