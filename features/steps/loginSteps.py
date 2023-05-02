from behave import *
from features.lib.pages.login_page import LoginPage
from features.lib.pages.loginlanding_page import LoginLanding
from helpers.loginhelper import loginDefault
from helpers.loginhelper import loginCustom
from helpers.loginhelper import loginBanned

import time


@given ('user is authenticated')
def user_authenticates(context):
    loginDefault(context)



@when('user enters correct credentials')
def user_enters_correct_credentials(context):
    loginDefault(context)

    print('User enters credentials and submits')


@when('user enters blank credentials')
def user_enters_blank_credentials(context):
    loginCustom(context,"","")

    print('User enters credentials and submits')

@when('user enters incorrect credentials')
def user_enters_incorrect_credentials(context):
    print('User enters credentials and submits')
    loginCustom(context,"incorrect","password")


@when('user logs in with "{name}" and "{pw}"')
def user_smoke_test(context, name, pw):
    print('User enters credentials and submits')
    loginCustom(context,name,pw)


@Then('Then user should {result}')
def user_smoke_test_result(context,result):
    context.execute_steps(u"""
        Then user should {result} button
    """.format(result=result))

@then('user should be authenticated')
def login_success(context):
    print('User should be authenticated')
    page = LoginLanding(context)
    assert page.logo
    print('User should be authenticated')

@then('user should not be authenticated')
def login_fail(context):
    page = LoginPage(context)
    assert page.login_error

@given ('I am on the Sauce Demo Login Page')
def openPage(context):
    page = LoginPage(context)
    page.visit(page.base_url)

@when('I fill the account information for account StandardUser into the Username field and the Password field')
def loginToPage(context):
    loginDefault(context)

@when('I click the Login Button')
def fakeclick(context):
     print('Here for feature file')

@then('I am redirected to the Sauce Demo Main Page')
def redirect(context):
    page = LoginLanding(context)
    assert context.browser.current_url == 'https://www.saucedemo.com/inventory.html'

@then('I verify the App Logo exists')
def logoCheck(context):
    page = LoginLanding(context)
    assert page.logo

@when('I fill the account information for account LockedOutUser into the Username field and the Password field')
def loginToPage(context):
    loginBanned(context)


@then('I verify the Error Message contains the text "{error}"')
def logoCheck(context, error):
    page = LoginPage(context)
    print( error + " ||| compare |||" + page.login_error.text )
    assert error in page.login_error.text
