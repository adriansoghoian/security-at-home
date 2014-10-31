__author__ = "Adrian Soghoian & Omar Ahmad"
import os, sys, subprocess, socket

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
	scan = subprocess.Popen(["nmap", "-sP", str(host)],stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
	scanlist = scan.split()
	print scanlist

	for i, each in enumerate(os_count):
		os = each[0]
		count = scanlist.count(os)

		if os == "Windows":
			os_count[i] = (os, count)
		elif os == "Apple":
			os_count[i] = (os, count)
		elif os == "Linux":
			os_count[i] = (os, count)
		else:
			os_count[i] = (os, count)

	return os_count

def scan_device(host):
	"""
	Conducts port scan of a specific device. 
	"""
	ports = []
	scan = subprocess.Popen(["nmap", str(host)],stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
	scanlist = scan.split()

	return True

def get_network_ip():
	# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	# s.connect(("finch.com",80))
	# ip = s.getsockname()[0]
	ip = "10.144.47.128"
	# s.close()
	return ip

def check_network():
	return True

ip = get_network_ip()
scan_network(ip)

