
from behave.fixture import use_fixture_by_tag
from selenium import webdriver
import os
from configparser import ConfigParser
from selenium.webdriver.common.keys import Keys
import time
#from helpers.helper_web import get_browser
from lib.pagefactory import on

def before_all(context):
    config = ConfigParser()
    print((os.path.join(os.getcwd(), 'setup.cfg')))
    configfile = (os.path.join(os.getcwd(), 'setup.cfg'))
    config.read(configfile)


    # read from cfg
    #helper_func = get_browser(config.get('Environment', 'Browser'))
    userLogin = config.get('UserCredentials','username')
    userPass = config.get('UserCredentials','password')
    bannedUser = config.get('UserCredentials','bannedusername')

    #context.helperfunc = helper_func
    context.userLogin = userLogin
    context.userPass = userPass
    context.bannedUser = bannedUser





# before every scenario
def before_scenario(context, scenario):
   print('Before scenario executed')

   context.browser = webdriver.Chrome()

   context.browser.maximize_window()
   print("Before scenario\n")
# after every feature
def after_feature(scenario, context):
   print('After feature executed')
   context.browser.quit()
# after all
def after_all(context):
   print('After all executed')
