__author__ = "Adrian Soghoian & Omar Ahmad"
import requests
import helpers
from splinter import Browser 

def is_router_secure():
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


