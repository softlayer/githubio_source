---
title: "get_firewall_for_a_vsi.py"
description: "get_firewall_for_a_vsi.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
tags:
    - "firewalls"
---


```
"""
Get the firewall associated to a VSI.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/findByIpAddress
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/getFirewallServiceComponent

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer
import json

USERNAME = 'set me'
API_KEY = 'set me'

vsiIp = "169.57.129.196"

client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
guestService = client['SoftLayer_Virtual_Guest']

try:
    vsi = guestService.findByIpAddress(vsiIp)
    firewall = guestService.getFirewallServiceComponent(id=vsi['id'])
    print(json.dumps(firewall, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to get the firewall. faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))

```
