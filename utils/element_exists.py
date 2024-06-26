from selenium.common.exceptions import NoSuchElementException

def element_exists(element_getter):
    try:
        element = element_getter()
        return element is not None
    except NoSuchElementException:
        return False