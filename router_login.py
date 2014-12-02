import csv

__author__ = "Adrian Soghoian & Omar Ahmad"
import requests
import helpers
from splinter import Browser 

def is_router_secure():
    """
    Returns a boolean indicating whether the user has updated their default login credentials. 
    """


#Variables for DIR-605L

user= 'admin' #not used here
pw = '' #YAY! encoding nothing!, for now
fake_pw = 'fadsas' #need to try something that doesn't work, to compare the results
def testDIR605L():
    credentials = helpers.get_default_credentials()[0]
    with Browser('phantomjs') as browser:
        url = 'http://192.168.0.1/'
        try:
            browser.visit(url)
            browser.fill('login_pass', credentials[1])
            button = browser.find_by_name('login')
            if browser.is_text_present('CURRENT NETWORK SETTING'):
                return False
            else:
                return True
        except:
            print "Probing the router admin page failed; perhaps the URL is incorrect."
            return True


