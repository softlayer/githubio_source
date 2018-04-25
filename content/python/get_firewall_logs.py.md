---
title: "get_firewall_logs.py"
description: "get_firewall_logs.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Subnet_IpAddress"
tags:
    - "firewalls"
---


```
"""
Get the firewall logs for an arbitrary IP address.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Subnet_IpAddress/getByIpAddress
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Subnet_IpAddress/getSyslogEventsOneDay

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer
import json

USERNAME = 'set me'
API_KEY = 'set me'

# The ip address to get the logs.
ip = "169.57.129.196"


client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
ipService = client['SoftLayer_Network_Subnet_IpAddress']

try:
    subnetIp = ipService.getByIpAddress(ip)
    logs = ipService.getSyslogEventsOneDay(id=subnetIp['id'])
    print(json.dumps(logs, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to get the logs. faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))

```
