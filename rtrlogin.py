__author__ = 'oza'

import requests
from splinter import Browser

#Variables for DIR-605L

user= 'admin' #not used here
pw = '' #YAY! encoding nothing!, for now
fake_pw = 'fadsas' #need to try something that doesn't work, to compare the results
def testDIR605L():
    with Browser('phantomjs') as browser:
         # Visit URL
         url = 'http://192.168.0.1/index.asp'
         browser.visit(url)
         browser.fill('login_pass', pw)
         button = browser.find_by_name('login')

         if browser.is_text_present('CURRENT NETWORK SETTING'):
             return True
         else:
             return False


if (testDIR605L()):
    r = requests.post("http://finch-security.herokuapp.com/notify")
