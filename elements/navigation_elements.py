from classes.Selector import Selector
from classes.Selector import SelectorType

class NavigationElements:
    
    SUBMIT_FLOW_NAV_BUTTON = Selector('''//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.View/android.view.View[2]''', SelectorType.XPATH)