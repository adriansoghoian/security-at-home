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
	report = models.Report(hosts)
	report.generate()

if __name__ == "__main__":
	ip = "10.128.4.147" # Omar's computer
	host = scanner.scan_device(ip)
	host.display_summary()
	write_report([host])

