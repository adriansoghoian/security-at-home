from pprint import pprint

__author__ = 'oza'

## Functions to help the package

import netifaces
import netaddr
import csv
import re
from uuid import getnode as get_mac

def get_manufacturer():
    mac = str(hex(get_mac()))[0:6]
    man_list = []
    print mac
    regex = re.compile("(?P<mac_add>[0-9A-Fa-f]{6})\s*.*(?P<man_name>.*)")
    with open('ref/oui.txt','r') as mac_file:
        for row in mac_file:
            m = regex.match(row)
            if m:
                man_list.append((m.group('mac_add'),(m.group('man_name'))))
    return man_list

def parse_info():
    """
    Takes the password list and parses
    :return:listOfTuples
    """
    pw_list = []
    with open('ref/Passwords.csv','r') as pwfile:
        pwread = csv.reader(pwfile)
        for row in pwread:
            if row[4].lower() == 'n/a' or 'blank' in row[4].lower():
                row[4] = ''
            if row[5].lower() == 'n/a' or 'blank' in row[5].lower():
                row[5] = ''
            pw_list.append(tuple(row))
    return pw_list

def get_models():
    parsed = parse_info()
    regex = re.compile('[^a-zA-Z0-9]')
    model_list = set()
    for router in parsed:
        if router[1]  != '':
            model_list.add(regex.sub('',router[1].lower()))
    return model_list


def parse_default_ip():
    """
    Takes the default IP list and parses
    :return:listOfTuples
    """
    ip_list = []
    with open('ref/default_ip.txt','r') as ipfile:
        ipread = csv.reader(ipfile, delimiter='\t')
        ipread.next()
        for row in ipread:
            ip_list.append(tuple(row))
    return ip_list

def get_user_pw():
    parsed = parse_info()
    combos = set()
    for router in parsed:
        if [router[4],router[5]] not in router:
            combos.add((router[4],router[5]))
    return combos

def get_user_pw_by_co(co_name,all_info=False):
    parsed = parse_info()
    regex = re.compile('[^a-zA-Z0-9]')
    co_name = co_name.lower()
    co_list = set()
    print co_name
    for router in parsed:
        rtr_co = router[0].lower()
        if (rtr_co == co_name
            or rtr_co in co_name
            or co_name in rtr_co):
                if all_info:
                    co_list.add(tuple(router))
                else:
                    co_list.add((router[4],router[5]))
    if regex.search(co_name):
        return co_list.union(get_user_pw_by_co(regex.sub('', co_name)))
    return co_list

def get_user_pw_by_model(model_name, co_name=None):
    regex = re.compile('[^a-zA-Z0-9]')
    model_name = regex.sub('', model_name.lower())
    if co_name:
        parsed = get_user_pw_by_co(co_name,True)
    else:
        parsed = parse_info()
    for router in parsed:
        rtr_name = regex.sub('',router[1].lower())
        print model_name,' ',rtr_name
        if (rtr_name != ''
            and rtr_name == model_name):
                return router[4],router[5]

def get_ip_by_co(co_name):
    ip_list = parse_default_ip()
    co_ip = set()
    co_name = co_name.lower()
    for ip in ip_list:
        ip_name = ip[0].lower()
        if (ip_name == co_name
            or ip_name in co_name
            or co_name in ip_name):
                co_ip.add((ip[4],ip[5]))
    return co_ip

global address
global netmask

def get_default_credentials():
    credentials = [ ('admin', '') ]
    return credentials

def get_ip():
    for iface in netifaces.interfaces():
        if netifaces.AF_INET in netifaces.ifaddresses(iface):
            add_info = netifaces.ifaddresses(iface)[netifaces.AF_INET]
            for addresses in add_info:
                if addresses['addr'].startswith('10.') or \
                    addresses['addr'].startswith('192.168.') or \
                    (addresses['addr'].startswith('172.') and int(addresses['addr'].split('.')[1]) in range(16,32)):
                        if 'netmask' in addresses and 'addr' in addresses and 'broadcast' in addresses :
                            netmask = addresses['netmask']
                            address = addresses['addr']
    return address,netmask

def get_gateway():
    ip_vals = get_ip()
    if netifaces.gateways()['default'][netifaces.AF_INET]:
        return netifaces.gateways()['default'][netifaces.AF_INET][0]

def ip_cidr():
    """
    Will calculate a CIDR-based IP address using the active interface's IP.
    Checking for IPs within the private network range, and that contain field AF_INET,
    and have a broadcast address, subnet mask, and IP address.
    (Virtual interfaces may be assigned a broadcast and IP address, and may also be active
    :return:String
    """
    ip_vals = get_ip()
    cidr = netaddr.IPNetwork('%s/%s' % (ip_vals[0], ip_vals[1]))
    return str(cidr.network) + '/' + str(cidr).split('/')[1]

if __name__ == "__main__":
    # print ip_cidr()
    # print parse_info()
    # print len(parse_info())
    # print get_gateway()
    # print get_user_pw()
    # for upw in get_user_pw():
    #     if upw[0].lower() == 'n/a' or 'blank' in upw[0].lower():
    #         print upw
    # print parse_default_ip()
    # print get_user_pw_by_co('D-link')
    # print len(get_user_pw_by_co('D-link'))
    # print get_user_pw_by_model('DIR-655')
    print get_models()
    print len(get_models())
    print get_manufacturer()
