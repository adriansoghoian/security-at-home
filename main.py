__author__ = "Adrian Soghoian & Omar Ahmad"

from router_login import is_router_secure
import scanner, models, helpers
import requests, datetime 
import models

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

def main(): 
	"""
	Overall method.  
	"""
	ip_range = helpers.ip_cidr()
	print ip_range
	gateway_ip = helpers.get_gateway()
	print gateway_ip

	active_hosts = scanner.scan_network(ip_range, gateway=gateway_ip)
	print len(active_hosts)
	for each in active_hosts:
		print each
	# host = scanner.scan_device(ip)
	report = models.Report(active_hosts)
	report.generate()

if __name__ == "__main__":
	main()

