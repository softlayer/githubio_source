---
title: "simplifiedOrder.py"
description: "simplifiedOrder.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
tags:
    - "dedicatedhost"
---


```
"""
Order a virtual server in a dedicated host.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/createObject
http://developer.softlayer.com/reference/services/SoftLayer_Virtual_Guest/getCreateObjectOptions

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer
import json

USERNAME = 'set me'
API_KEY = 'set me'

client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
virtualGuestService = client['SoftLayer_Virtual_Guest']

# The order template for the new virtual guest
# See getCreateObjectOptions for available options
order = {
    "hostname": "dedisim2",
    "domain": "example.com",
    "blockDevices": [
        {
            "device": "0",
            "diskImage": {
                "capacity": 25
            }
        }
    ],
    "localDiskFlag": True,
    "datacenter": {
        "name": "dal10"
    },
    "startCpus": 4,
    "dedicatedHost": {
        "id": 9301
    },
    "maxMemory": 8192,
    "operatingSystemReferenceCode": "UBUNTU_LATEST"
}

try:
    response = virtualGuestService.createObject(order)
    print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to place the order. faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))

```
