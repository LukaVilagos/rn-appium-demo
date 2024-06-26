from enum import Enum
from appium.webdriver.common.appiumby import AppiumBy

class SelectorType(Enum):
    XPATH = 'xpath'
    ACCESSIBILITY_ID = 'accessibility_id'
    CLASS_NAME = 'class_name'
    CSS_SELECTOR = 'css_selector'
    ID = 'id'
    IMAGE = 'image'
    IOS_CLASS_CHAIN = 'ios_class_chain'
    

class Selector:
    def __init__(self, value, type : SelectorType) -> None:
        self.value = value
        self.type = type