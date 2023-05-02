
from selenium.webdriver.common.by import By
from features.lib.pages.base_page import BasePage


class LoginPage(BasePage):
    locator_dictionary = {
        "email": (By.CSS_SELECTOR, "[data-test='username']"),
        "password": (By.CSS_SELECTOR, "[data-test='password']"),
        "signin_button": (By.CSS_SELECTOR, "[data-test='login-button']"),
        "login_error": (By.CSS_SELECTOR, "[data-test='error']")
    }

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser,
            base_url='https://www.saucedemo.com/')
