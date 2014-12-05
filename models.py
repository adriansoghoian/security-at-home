import reference, datetime 
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

class Report:
	title = "Canary Cyber Security Report"

	def __init__(self, hosts):
		self.hosts = hosts
		self.title = str(datetime.datetime.now()) + ".pdf"
		self.template = SimpleDocTemplate("reports/" + self.title,pagesize=letter,
                        rightMargin=72,leftMargin=72,
                        topMargin=72,bottomMargin=18)
		self.styles = getSampleStyleSheet()

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

		string = "<font size=16><b>Your devices:</b></font>"
		Story.append(Paragraph(string, self.styles['Normal']))
		Story.append(Spacer(1, 16))

		for host in self.hosts:
			print host.number
			string = "<font size=12><b>Number of open ports:</b> " + str(len(host.open_ports)) + ". "
			if len(host.open_ports) > 0:
				string += "Please seek ways to close more ports. "
			Story.append(Paragraph(string, self.styles['Normal']))
			Story.append(Spacer(1, 12))

		self.template.build(Story)

class Host:
	count = 0

	def __init__(self, os="Unknown", ip="Unkown", manufacturer="Unknown", mac_address="Unknown", open_ports=[], is_down=False):
		self.os = os
		self.ip = ip
		self.manufacturer = manufacturer
		self.open_ports = open_ports
		self.mac_address = mac_address
		self.is_router = False
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

class Port:

	def __init__(self, number, port_service, port_status):
		self.number = number
		self.number = number
		self.port_service = port_service
		self.port_status = port_status
