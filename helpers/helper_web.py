from selenium import webdriver
from helpers.seleniumhelper import HelperFunc

def get_browser(browser):
    if browser == "chrome":
        return HelperFunc(webdriver.Chrome())
