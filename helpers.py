from pprint import pprint

__author__ = 'oza'

## Functions to help the package

import netifaces
import netaddr
import csv


def parse_info():
    """
    Takes the password list and parses
    :return:listOfTuples
    """
    pw_list = []
    with open('ref/Passwords.csv','r') as pwfile:
        pwread = csv.reader(pwfile)
        for row in pwread:
            if row[3:5]:
                if row[3] == 'HTTP':
                    pw_list.append(tuple(row[0:6]));
    return pw_list[3:]


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
    print ip_cidr()
    print parse_info()
    print get_gateway()
