__author__ = "Adrian Soghoian & Omar Ahmad"

from router_login import is_router_secure
import scanner, models, helpers
import requests, datetime 

def update_server(os_list, router_secure):
	"""
	Legacy code. Remove at some point. 
	"""
	if router_secure:
		router_status = "Secure"
	else:
		router_status = "Insecure"

	os_list = "_".join(os_list)
	payload = {'router_status': router_status, 'key2': os_list}
	requests.post("http://finch-security.herokuapp.com/refresh", data=payload)

def get_nvd_results(host):
	manufacturer_str = host.manufacturer
	if " " in manufacturer_str:
		manufacturer_str = manufacturer_str.replace(" ", "+")
	url = "https://web.nvd.nist.gov/view/vuln/search-results?query=%s&search_type=all&cves=on" % (manufacturer_str)
	return url

def write_report(hosts): ## TODO - write method that generates text file. 
	"""
	Overall method that constructs the summary document. 
	"""
	date = datetime.datetime.now()
	title = "Canary Security at Home: " + str(date)
	f = open(title, 'w')

	# Summary
	f.write("Hello. You have this many devices connected to your network: %s" % (models.Host.return_num_hosts()))
	f.write("\n")
	f.write("\n")

	# Host-specific information
	for each in hosts:
		os, mac, manufacturer, ports = each.os, each.mac_address, each.manufacturer, each.open_ports
		f.write("Here is a summary for a connected device with MAC address: %s." % (mac))
		f.write("\n")
		f.write("It's OS is %s. It's manufacturer is %s. It has this many open ports: %s." % (os, manufacturer, ports))
		f.close()

if __name__ == "__main__":

	ip = "10.144.1.142" # Omar's computer
	host = scanner.scan_device(ip)
	host.display_summary()
	write_report([host])

