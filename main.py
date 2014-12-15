import router_login

__author__ = "Adrian Soghoian & Omar Ahmad"

import scanner
import helpers
import models

import emailPDF


def main():
    """
	Overall method.  
	"""
    ip_range = helpers.ip_cidr()
    print ip_range
    gateway_ip = helpers.get_gateway()
    router_status = router_login.is_router_secure()
    print gateway_ip

    active_hosts = scanner.scan_network(ip_range, gateway=gateway_ip)
    print "The number of active hosts is: " + len(active_hosts)
    print "Here are the active hosts: "
    for each in active_hosts:
        print each
    # host = scanner.scan_device(ip)
    report = models.Report(active_hosts, router_status=router_status)
    report.generate()
    if emailPDF.is_rpi():
        emailPDF.send()


if __name__ == "__main__":
    main()

