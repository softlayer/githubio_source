---
title: "get_passwrods_for_a_vsi.py"
description: "get_passwrods_for_a_vsi.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
tags:
    - "managepassword"
---


```
"""
Get the passwords for a vsi.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/getSoftwareComponents

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer
import json

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'

vsiId = 13102629

client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
vsiService = client['SoftLayer_Virtual_Guest']

objectMask = 'mask[passwords,softwareLicense]'

try:
    components = vsiService.getSoftwareComponents(id=vsiId, mask=objectMask)
    print(json.dumps(components, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to get the passwords faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))
    exit(1)

```
