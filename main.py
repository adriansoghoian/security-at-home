__author__ = "Adrian Soghoian & Omar Ahmad"

from router_login import is_router_secure
import scanner, requests, helpers

def update_server(os_list, router_secure):
	if router_secure:
		router_status = "Secure"
	else:
		router_status = "Insecure"

	os_list = "_".join(os_list)
	payload = {'router_status': router_status, 'key2': os_list}
	requests.post("http://finch-security.herokuapp.com/refresh", data=payload)

def generate_report():
	router_status = is_router_secure()
	ip = helpers.ip_cidr()
	hosts = scanner.scan_network(ip)

if __name__ == "__main__":
	generate_report()


	os_list = scanner.scan_network(ip)

	update_server(os_list, router_secure)
