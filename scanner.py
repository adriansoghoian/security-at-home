__author__ = "Adrian Soghoian & Omar Ahmad"

import os, sys, subprocess, socket
import helpers
from IPy import IP

"""
This subsystem contains functionality to scan the local network for connected 
devices, their OS fingerprints, and any open ports that they may have. 
"""

def scan_network(host):
	"""
	This method scans a given host and collects information on all the hosts currently
	connected, along with their OS. 
	"""
	os_strings = [ "Windows", "Apple", "IOS", "Linux", "Unknow" ]
	win, apple, linux, ios, unknow = [ (os_strings[i], 0) for i in range(len(os_strings)) ]
	os_count = [ win, apple, linux, ios, unknow ]
	devices = []

	scan = subprocess.Popen(["nmap", "-PR", str(host)],stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
	scanlist = scan.split()
	if scanlist.count("up") > 0:
		indices = [i + 2 for i, x in enumerate(scanlist) if x == "report"]
		ip_list = [ scanlist[i] for i in indices ]
	
	for ip in ip_list:
		devices.append(scan_device(ip))
	print devices
	return devices

def scan_device(ip):
	"""
	Generates an OS fingerprint for a given host. 
	"""
	scan = subprocess.Popen(["nmap", "-O", str(ip)],stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
	scanlist = scan.split()
	os_index = scanlist.index("Running:") + 1

	if scanlist[os_index] == "Windows":
		return "Windows"
	elif scanlist[os_index] == "Apple":
		return "Apple"
	elif scanlist[os_index] == "Linux":
		return "Linux"
	else:
		return "Unknow"

if __name__ == "__main__":
	ip = helpers.ip_cidr()
	scan_network(ip)

