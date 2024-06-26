from classes.Selector import Selector
from classes.Selector import SelectorType

class SubmitElements:
    
    #region General
    
    HEADING = Selector('''//android.widget.TextView[@text="Submit a reservation"]''', SelectorType.XPATH)
    PARAGRAPH = Selector('''//android.widget.TextView[@text="Submit a reservation you can't make and earn a premium token if it gets approved."]''', SelectorType.XPATH)
    PROGRESS_BAR = Selector('''//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup''', SelectorType.XPATH)
    GO_BACK_BUTTON = Selector('''//android.widget.HorizontalScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]''', SelectorType.XPATH)
    
    #endregion
    
    #region 1st screen
    
    CHANGE_CITY_MENU_NEW_YORK_BUTTON = Selector('''New York''', SelectorType.ACCESSIBILITY_ID)
    CHANGE_CITY_MENU_MIAMI_BUTTON = Selector('''Miami''', SelectorType.ACCESSIBILITY_ID)
    CHANGE_CITY_MENU_ARROW = Selector('''//android.view.ViewGroup[@content-desc="Miami"]/com.horcrux.svg.SvgView''', SelectorType.XPATH)
    SCREEN_ONE_SUBHEADING = Selector('''//android.widget.TextView[@text="Where is the reservation?"]''', SelectorType.XPATH)
    SEARCH_RESTAURANTS_INPUT = Selector('''android.widget.EditText''', SelectorType.CLASS_NAME)
    WHEN_BUTTON = Selector('''When''', SelectorType.ACCESSIBILITY_ID)
    
    # Search restaurants result
    
    SEARCH_RESTAURANTS_TOP_RESULT = Selector('''//android.widget.HorizontalScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup''', SelectorType.XPATH)
    SEARCH_RESTAURANTS_12_CHAIRS_CAFE_RESULT = Selector('''12 Chairs Cafe, Wythe Ave, Brooklyn''', SelectorType.ACCESSIBILITY_ID)
    
    # Restaurant selected
    
    INDOOR_BUTTON = Selector('''Indoor''', SelectorType.ACCESSIBILITY_ID)
    OUTDOOR_BUTTON = Selector('''Outdoor''', SelectorType.ACCESSIBILITY_ID)
    DETAILS_INPUT_EMPTY = Selector('''//android.widget.EditText[@text="Ex: Covered Patio, Bar, Chef's Counter"]''', SelectorType.XPATH)
    
    # Enter City Menu
    
    NEW_YORK_CITY_SELECT_BUTTON = Selector('''//android.widget.TextView[@text="New York"]''', SelectorType.XPATH)
    MIAMI_CITY_SELECT_BUTTON = Selector('''//android.widget.TextView[@text="Miami"]''', SelectorType.XPATH)
    
    #endregion
    
    #region 2nd screen
    
    SCREEN_TWO_SUBHEADING = Selector('''//android.widget.TextView[@text="When is the reservation?"]''', SelectorType.XPATH)
    SELECT_DATE_INPUT_EMPTY = Selector('''Select Date''', SelectorType.ACCESSIBILITY_ID)
    SELECT_TIME_INPUT_EMPTY = Selector('''Select Time''', SelectorType.ACCESSIBILITY_ID)
    TIMEZONE_INFO = Selector('''//android.widget.TextView[@text="Make sure the date and time match what is listed on your reservation. All times are local to New York (EST)."]''', SelectorType.XPATH)
    WHO_BUTTON = Selector('''Who''', SelectorType.ACCESSIBILITY_ID)
    
    #endregion