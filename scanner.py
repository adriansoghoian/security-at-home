__author__ = "Adrian Soghoian & Omar Ahmad"
import os, sys, subprocess, socket
from IPy import IP

"""
This subsystem contains functionality to scan the local network for connected 
devices, their OS fingerprints, and any open ports that they may have. 
"""

def scan_network(host):
    scan = subprocess.Popen(["nmap", "-PE","-PP","-PS21,22,23,25,80,443,3306,3389,8080", str(host)],stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
    print scan
    print "*********"
    scanv = subprocess.Popen(["nmap", "-PR", "-O", str(host)],stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
    print scanv
    return True

def scan_device():
	return True

def get_network_ip():
	# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	# s.connect(("finch.com",80))
	# ip = s.getsockname()[0]
	ip = "192.168.0.0/24"
	# s.close()
	return ip

def check_network():
	return True

ip = get_network_ip()
scan_network(ip)

