"""
These are used to parse the NEXT SERVICE FINGERPRINT fingerprint outputted by Nmap
in case the OS fingerprint fails. The keywords are mapped to various known OSes that 
sometimes fail Nmap detection. 
"""
OS_TYPES = { "apple": "Mac OS X" }
