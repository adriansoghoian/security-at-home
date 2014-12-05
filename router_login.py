import csv

__author__ = "Adrian Soghoian & Omar Ahmad"
import helpers
from splinter import Browser
from bs4 import BeautifulSoup

# instantiate the parser and fed it some HTML

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

def testRouter():
    with Browser('phantomjs') as browser:
        url = 'http://' + helpers.get_gateway()
        print url
        try:
            browser.visit(url)
            soup = BeautifulSoup(browser.html)
            print soup.form.find_all('input')
            print soup.find(value='admin') #if value is there for admin, but field is hidden, don't touch it
            for ids in soup.form.find_all('input'):
                if ids.get('type') != 'hidden':
                    print ids.get('id'),' ',ids.get('type')


        except:
            print "Probing the router admin page failed; perhaps the URL is incorrect."
            return True


if __name__ == "__main__":
    testRouter()