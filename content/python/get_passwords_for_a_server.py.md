---
title: "get_passwords_for_a_server.py"
description: "get_passwords_for_a_server.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Hardware_Server"
tags:
    - "managepassword"
---


```
"""
Get the passwords for a server.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server
http://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server/getSoftwareComponents

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer
import json

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'

serverId = 179996

client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
serverService = client['SoftLayer_Hardware_Server']

objectMask = 'mask[passwords,softwareLicense]'

try:
    components = serverService.getSoftwareComponents(id=serverId, mask=objectMask)
    print(json.dumps(components, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to get the passwords faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))
    exit(1)

```
