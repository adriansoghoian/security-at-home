import reference, datetime 
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

class Report:
	title = "Canary Cyber Security Report"

	def __init__(self, hosts):
		self.hosts = hosts
		self.title = str(datetime.datetime.now()) + ".pdf"
		self.template = SimpleDocTemplate("reports/" + self.title,pagesize=letter,
                        rightMargin=72,leftMargin=72,
                        topMargin=72,bottomMargin=18, 
                        font ='Courier',fontSize=12)
		self.styles = getSampleStyleSheet()

	@classmethod
	def get_nvd_url(cls, host):
		manufacturer_str = host.manufacturer
		if " " in manufacturer_str:
			manufacturer_str = manufacturer_str.split(" ")[0]
		url = "https://web.nvd.nist.gov/view/vuln/search-results?query=%s&search_type=all&cves=on" % (manufacturer_str)
		return url

	def generate(self):
		Story = []
		logo = "canary.png"
		self.styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))

		title = "<font size=24><b>%s</b></font>" % (Report.title)
		Story.append(Paragraph(title, self.styles['Normal']))
		Story.append(Spacer(1, 24))

		string = """<font size=12>Here is a status report about your home network. 
				 Please review it and follow up with appropriate actions. 
				 Remember that over two third of personal network intrusions occur 
				 due to weak passwords on your routers and devices.</font>"""
		Story.append(Paragraph(string, self.styles['Normal']))
		Story.append(Spacer(2, 12))

		sorted(self.hosts, key=type, reverse=True)

		for i, host in enumerate(self.hosts):
			if host.mac_address != "Unknown":
				if i == 0:
					string = "<font size=16><b>Your router:</b></font>"
					Story.append(Paragraph(string, self.styles['Normal']))
					Story.append(Spacer(1, 16))
					string = "<font size=12><b>Admin Page Status: </b>" + "TBD</font>"

				if i == 1: 
					string = "<font size=16><b>Your devices:</b></font>"
					Story.append(Paragraph(string, self.styles['Normal']))
					Story.append(Spacer(1, 16))

				string ="<font size=12><b>MAC Address:</b> " + host.mac_address
				Story.append(Paragraph(string, self.styles['Normal']))
				Story.append(Spacer(1, 12))

				string = "<font size=12><b>IP Address:</b> " + host.ip + "</font>"
				Story.append(Paragraph(string, self.styles['Normal']))
				Story.append(Spacer(1, 12))

				string = "<font size=12><b>Manufacturer:</b> " + host.manufacturer + "</font>"
				Story.append(Paragraph(string, self.styles['Normal']))
				Story.append(Spacer(1, 12))

				if host.manufacturer != "Unknown":
					string = """<font size=12><b>Major issues associated with manufacturer:</b> 
							 Please check out the <a href='%s' color='blue'>National Vulnerability 
							 Database</a> for a list of current issues related to %s products.</font>
							 """ % (Report.get_nvd_url(host), host.manufacturer)
					Story.append(Paragraph(string, self.styles['Normal']))
					Story.append(Spacer(1, 12))

				string = "<font size=12><b>Number of open ports:</b> " + str(len(host.open_ports)) + ".</font>" 
				if len(host.open_ports) > 0:
					string += "Please seek ways to close more ports. " 
					Story.append(Paragraph(string, self.styles['Normal']))
					Story.append(Spacer(1, 12))
					port_data = [["NUMBER", "SERVICE", "NOTES"]]
					for port in host.open_ports:
						row = []
						row.append(port.number)
						row.append(port.port_status)
						row.append("TBD")
						port_data.append(row)
					port_table = Table(port_data)
					Story.append(port_table)
					Story.append(Spacer(3, 12))
				if i > 0 and i < len(self.hosts) - 1:
					Story.append(Paragraph("###########################################", self.styles['Normal']))
		self.template.build(Story)

class Host:
	count = 0

	def __init__(self, os="Unknown", ip="Unknown", manufacturer="Unknown", mac_address="Unknown", open_ports=[], is_down=False):
		self.os = os
		self.ip = ip
		self.manufacturer = manufacturer
		self.open_ports = open_ports
		self.mac_address = mac_address
		self.is_down = False
		Host.count += 1

	def add_port(self, port):
		self.open_ports.append(port)

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
				port_string += str(each.number) + " "
		else:
			port_string = "None detected yet."
		print "OS: ", self.os, ",manufacturer: ", self.manufacturer, ", MAC Address: ", self.mac_address, ", Ports: ", port_string

class Router(Host):

	def __init__(self, is_secured=False, os="Unknown", ip="Unknown", manufacturer="Unknown", mac_address="Unknown", open_ports=[], is_down=False):
		Host.__init__(self, os, ip, manufacturer, mac_address, open_ports, is_down)
		self.is_secured = is_secured

class Port:

	def __init__(self, number, port_service, port_status):
		self.number = number
		self.port_service = port_service
		self.port_status = port_status
