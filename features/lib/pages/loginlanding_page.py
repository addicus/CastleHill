
from selenium.webdriver.common.by import By
from features.lib.pages.base_page import BasePage


class LoginLanding(BasePage):
    locator_dictionary = {
        "logo": (By.CLASS_NAME, 'app_logo')

    }

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser,
            base_url='https://www.saucedemo.com/inventory.html')
