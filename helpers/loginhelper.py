import time
from features.lib.pages.login_page import LoginPage


def loginDefault(context):

    page = LoginPage(context)
    page.email.send_keys(context.userLogin)
    page.password.send_keys(context.userPass)
    page.signin_button.click()
    print("Login")

def loginBanned(context):

    page = LoginPage(context)
    page.email.send_keys(context.bannedUser)
    page.password.send_keys(context.userPass)
    page.signin_button.click()
    print("Login")



def loginCustom(context,username,password):

    page = LoginPage(context)
    page.email.send_keys(username)
    page.password.send_keys(password)
    page.signin_button.click()
