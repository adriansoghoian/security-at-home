__author__ = 'oza'

#import requests
#import urllib3
#import mechanize

#from requests import Request,Session
from splinter import Browser
from zope.testbrowser.browser import Browser as zbrow
import datetime
import base64

import sys, logging
logger = logging.getLogger("mechanize")
logger.addHandler(logging.StreamHandler(sys.stdout))
logger.setLevel(logging.DEBUG)

def unix_time(dt):
    epoch = datetime.datetime.utcfromtimestamp(0)
    delta = dt - epoch
    return delta.total_seconds()

def unix_time_millis(dt):
    return unix_time(dt) * 1000.0


#Variables for DIR-605L
date = str(int(unix_time(datetime.datetime.now())*1000))
ver = ''
verc = ''
filecode = ''
user= 'admin'
pw = '' #YAY! encoding nothing!, for now
fake_pw = 'fadsas' #need to try something that doesn't work, to compare the results

#zb = zbrow()
with Browser('phantomjs') as browser:
     # Visit URL
     url = 'http://192.168.0.1/index.asp'
     browser.visit(url)
     browser.fill('login_pass', pw)
     button = browser.find_by_name('login')

     if browser.is_text_present('CURRENT NETWORK SETTING'):
         print "We hackz0r3d your router"
     else:
         print "Good job, you changed the password"
