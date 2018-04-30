---
title: "ListDedicatedHost.py"
description: "ListDedicatedHost.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Virtual_DedicatedHost"
tags:
    - "dedicatedhost"
---


```
"""
List the dedicated hosts in the account.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Account/getDedicatedHosts
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_DedicatedHost

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer
import json

USERNAME = 'setme'
API_KEY = 'setme'

client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
accountService = client['SoftLayer_Account']

try:
    response = accountService.getDedicatedHosts()
    print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to list the dedicated hosts. faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))

```
