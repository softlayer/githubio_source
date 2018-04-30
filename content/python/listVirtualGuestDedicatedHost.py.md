---
title: "listVirtualGuestDedicatedHost.py"
description: "listVirtualGuestDedicatedHost.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_DedicatedHost"
tags:
    - "dedicatedhost"
---


```
"""
List associated guest of dedicated host.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_DedicatedHost/getGuests
http://sldn.softlayer.com/reference/datatypes/SoftLayer_virtual_guest

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer
import json

USERNAME = 'set me'
API_KEY = 'set me'

client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
dedicatedHostService = client['SoftLayer_Virtual_DedicatedHost']
dedicatedHostId = 9301

try:
    response = dedicatedHostService.getGuests(id=9301)
    print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to get the guests. faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))




```
