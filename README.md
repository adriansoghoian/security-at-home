security-at-home
================

This module runs network vulnerability scans and saves a PDF summary of the result locally on your machine. The primary scanning functionality uses base scans from NMAP, the canonical open-source network scanner. For certain wifi router models it will also probe the administrative page to see if it's been secured beyond the default username / password combination.

INSTALLATION:

This module will work on a Raspberry Pi/Pi2 running Raspbian. In order to get it working, it will require the installation of several packages...

python-dev maybe required for installing one or more of the following Python packages

nmap is a required install - it can be installed using apt-get

phantomjs is a required install - there are several binary distributions of phantomjs, install one to a PATH directory or add it to your PATH.

The following Python packages are required:

netifaces (may require compiling from source)
netaddr
reportlab
pyzmail (this is an asset added for demonstration purposes, but may come in handy)
splinter
requests
beautifulsoup4
