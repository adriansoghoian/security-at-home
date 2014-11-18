class Host:
	count = 0

	def __init__(self, os="Unkown", manufacturer="Unkown", mac_address="Unknown", open_ports="Unknown"):
		self.os = os
		self.manufacturer = manufacturer
		self.open_ports = open_ports
		self.mac_address = mac_address
		Host.count += 1

	def display_summary(self):
		if self.open_ports != "Unkown":
			ports = ""
			for each in self.open_ports:
				ports += str(each) + " "
		else:
			"None detected yet."
		print "OS: ", self.os, ", manufacturer: ", self.manufacturer, ", MAC Address: ", self.mac_address, ", Ports: ", ports