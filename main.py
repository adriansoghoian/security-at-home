import router_login

__author__ = "Adrian Soghoian & Omar Ahmad"

import requests

import scanner
import helpers
import models

import emailPDF

def main():
    """
    Overall method.
    """
    ip_range = helpers.ip_cidr()
    print "The ip range scanning over is: ", ip_range
    gateway_ip = helpers.get_gateway()
    print "The gateway IP is: ", gateway_ip
    active_hosts = scanner.scan_network(ip_range, gateway=gateway_ip)
    print "There are %s many active hosts detected." % (len(active_hosts))
    print "Here are the active host IPs: "
    for each in active_hosts:
        print each.ip
    # host = scanner.scan_device(ip)
    report = models.Report(active_hosts)
    report.generate()
    if emailPDF.is_rpi():
        emailPDF.send()

if __name__ == "__main__":
    main()

