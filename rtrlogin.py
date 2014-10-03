__author__ = 'oza'

import requests
import urllib3
import mechanize

from requests import Request,Session
import datetime
import base64

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
pw = base64.b16encode('') #YAY! encoding nothing!, for now
fake_pw = 'fadsas' #need to try something that doesn't work, to compare the results

browser= mechanize.Browser()
browser.open('http://192.168.0.1/index.asp')
browser.select_form("myform")
print browser.form

#browser.set_value(user, name="login_n", id="login_n")
browser.set_value(pw, name="login_pass")
browser.set_value('', name="VER_CODE")
#browser.set_value(date, name="curTime")
response1 = browser.submit()


assert browser.viewing_html()
print browser.title()
print response1.geturl()
#print response1.info()  # headers
#print response1.read()  # body

# s = Session()
#
#
# payload = {
#     'id':'myform',
#     'name':'myform',
#     'onsubmit':'check()',
#     'action':'/goform/formLogin',
#     'login_name':'',
#     'login_n':user,
#     'login_pass':pw,
#     'curTime':date,
#     'FILECODE':filecode,
#     'VERIFICATION_CODE':ver,
#     'VER_CODE':verc
# }
#
# print payload
#
# headers = {
#     'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#     'Origin': 'http://www.indiapost.gov.in',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.17 (KHTML, like Gecko)  Chrome/24.0.1312.57 Safari/537.17',
#     'Content-Type': 'application/x-www-form-urlencoded',
#     'Referer': 'http://192.168.0.1/index.asp',
#     'Accept-Encoding': 'gzip,deflate,sdch',
#     'Accept-Language': 'en-US,en;q=0.8',
#     'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3'
# }
#
# item_request_headers = {
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0",
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip,deflate",
#     "Accept-Language": "en-US,en;q=0.5"
# }
#
#
# post_request = Request('POST', 'http://192.168.0.1/index.asp',headers=item_request_headers,data=payload)
# prepare_post = s.prepare_request(post_request)
# post_response = s.send(prepare_post)
#
# get_request = Request('GET', 'http://192.168.0.1/Basic/Wizard_Tp_WanDetect_Login.asp?t='+date)
# prepare_get = s.prepare_request(get_request)
# get_response = s.send(prepare_get)
# #r = requests.get('http://192.168.0.1/index.asp',params=userpw)
#
# #p = requests.post('http://192.168.0.1/goform/formLogin',params=userpw)
# #p = requests.post('http://192.168.0.1/Basic/Wizard_Tp_WanDetect_Login.asp?t=1412300839270',params=userpw)
#
#
# print post_response.text
# print get_response.text
# #print p.text