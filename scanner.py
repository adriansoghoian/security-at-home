__author__ = "Adrian Soghoian & Omar Ahmad"

import os, sys, subprocess, socket, reference, models
import helpers
from IPy import IP

"""
This subsystem contains functionality to scan the local network for connected 
devices, their OS fingerprints, and any open ports that they may have. 
"""

def scan_network(range):
	"""
	This method scans a given IP range and collects information on all of the hosts currently
	connected, along with their OS. 
	"""
	os_strings = [ "Windows", "Apple", "IOS", "Linux", "Unknow" ]
	win, apple, linux, ios, unknow = [ (os_strings[i], 0) for i in range(len(os_strings)) ]
	os_count = [ win, apple, linux, ios, unknow ]
	devices = []

	scan = subprocess.Popen(["nmap", "-PR", str(range)],stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
	scanlist = scan.split()
	if scanlist.count("up") > 0:
		indices = [i + 2 for i, x in enumerate(scanlist) if x == "report"]
		ip_list = [ scanlist[i] for i in indices ]
	
	for ip in ip_list:
		devices.append(scan_device(ip))
	return devices

def extract_manufacturer(scanlist):
	"""
	Pulls out the manufacturer name from the scan output. 
	"""
	index = scanlist.index("Address:") + 1
	substring = " ".join(scanlist[index + 1:index + 5])
	manufacturer = substring[substring.find("(") + 1:substring.find(")")]
	return manufacturer.strip()

def extract_mac_address(scanlist):
	"""
	Extracts MAC address from the scan output. 
	"""
	mac_address_index = scanlist.index("Address:") + 1
	mac_address = scanlist[mac_address_index]
	return mac_address.strip()

def extract_ports(scanlist):
	"""
	Extracts port information from the scan output. 
	"""
	scan = " ".join(scanlist)
	if " are closed" in scan:
		return []
	else:
		port_index = 
		return ["3000"]

def scan_device(ip):
	"""
	Generates an OS fingerprint for a given host. 
	"""
	scan = subprocess.Popen(["nmap", "-sS", str(ip)],stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
	scanlist = scan.split()
	print scan

	if "Host seems down" in scan:
		return models.Host(is_down=True)
	mac_address = extract_mac_address(scanlist)
	manufacturer = extract_manufacturer(scanlist)
	ports = extract_ports(scanlist)

	try:
		os_index = scanlist.index("Running:") + 1
		os_type = scanlist[os_index]
	except ValueError:
		os_type = "Unknown"
		for each in reference.OS_TYPES:
			if each in scan:
				os_type = reference.OS_TYPES[each]

	return models.Host(os_type, manufacturer, mac_address)
