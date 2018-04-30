---
title: "firewall_report.py"
description: "firewall_report.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Subnet_IpAddress"
tags:
    - "firewalls"
---


```
"""
Get firewall report

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Subnet_IpAddress
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Subnet_IpAddress/getTopTenSyslogEventsByProtocolsOneDay
"""
import SoftLayer

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'

# The ip address ID you which to generate the report
ipAddressId = 12597032

# Declare the API client
client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)

try:
    # Getting the report
    result = client['SoftLayer_Network_Subnet_IpAddress'].getTopTenSyslogEventsByProtocolsOneDay(id=ipAddressId)
    print(result)
except SoftLayer.SoftLayerAPIError as e:
    # If there was an error returned from the SoftLayer API then bomb out with the
    # error message.
    print("Unable to get the firewall report faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))

```
