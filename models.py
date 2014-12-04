import reference

class Host:
	count = 0

	def __init__(self, os="Unknown", manufacturer="Unknown", mac_address="Unknown", open_ports=[], is_down=False):
		self.os = os
		self.manufacturer = manufacturer
		self.open_ports = open_ports
		self.mac_address = mac_address
		self.is_router = False
		self.is_down = False
		Host.count += 1

	def add_port(self, port):
		self.open_ports.append(port)

	### TODO - write method that detects which host is the router
	### And flips the self.is_router flag to True.
	@classmethod
	def flag_router(cls, hosts):
		for each in hosts:
			return True

	@classmethod
	def return_num_hosts(cls):
		return str(cls.count)

	def display_summary(self):
		port_string = ""
		if len(self.open_ports) > 0:
			for each in self.open_ports:
				port_string += str(each) + " "
		else:
			port_string = "None detected yet."

		print "OS: ", self.os, ",manufacturer: ", self.manufacturer, ", MAC Address: ", self.mac_address, ", Ports: ", port_string

class Port:

	def __init__(self, number, port_type, reference_link="temp"):
		self.number = number
		self.type = port_type
		reference_link = reference.PORT_REFERENCE[number]
