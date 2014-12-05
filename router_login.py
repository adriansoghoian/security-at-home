import csv
import re

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
    global html
    global soup
    with Browser('phantomjs') as browser:
        url = 'http://' + helpers.get_gateway()
        print url
        try:
            browser.visit(url)
            html = browser.html
            soup = BeautifulSoup(browser.html)
            print soup.find_all('input')
            print soup.find_all('form')

        except:
            print "Probing the router admin page failed; perhaps the URL is incorrect."
            return True
    return None

def input_fields():
    input_fields = []
    for inputs in soup.form.find_all('input'):
        if inputs.get('type') != 'hidden':
            input_fields.append(inputs.get('id'))
    return input_fields


def option_field():
    select = []
    for options in soup.find_all('select'):
        select.append(options.get('name'))
        option_values = []
        for option in options.find_all('option'):
            option_values.append(option.get('value'))
        select.append(option_values)
    return select


def user_field(user_name):
    return None



def pw_field(pw):
    return None

def find_model():
    model_cand = []
    regex = re.compile('[^a-zA-Z0-9]')
    html_parse = regex.sub('',html.lower())
    for model in helpers.get_models():
        if model in html_parse:
            model_cand.append(model)
    return model_cand

if __name__ == "__main__":
    testRouter()
    print option_field()
    print input_fields()
    print find_model()