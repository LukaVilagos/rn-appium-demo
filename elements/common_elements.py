from elements.selector import Selector
from elements.selector import SelectorType

class CommonElements:
    
    #region android
    
    ANDROID_OK_BUTTON = Selector('''android:id/button1''', SelectorType.ID)
    ANDROID_CANCEL_BUTTON = Selector('''android:id/button2''', SelectorType.ID)
    
    #endregion
    
    #region app
    
    CLOSE_MENU_BUTTON = Selector('''com.horcrux.svg.SvgView''', SelectorType.CLASS_NAME)
    
    #endregion