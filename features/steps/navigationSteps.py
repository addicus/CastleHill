from behave import *
from features.lib.pages.login_page import LoginPage




@given('user is on login screen')
def user_opens_login(context):
    page = LoginPage(context)
    page.visit(page.base_url)
    print('User is on login screen')
