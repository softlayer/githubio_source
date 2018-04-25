---
title: "list_servers_to_order_hourly.py"
description: "list_servers_to_order_hourly.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Product_Package_Server"
tags:
    - "baremetalservers"
---


```
"""
List all the servers to order (hourly).

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Package_Server/getAllObjects
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Package_Server/
http://sldn.softlayer.com/article/Object-Filters

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer
import json

# Your SoftLayer API username and key.
API_USERNAME = 'set-me'

# Generate one at https://control.softlayer.com/account/users
API_KEY = 'set-me'

client = SoftLayer.create_client_from_env(username=API_USERNAME, api_key=API_KEY)
packageService = client['SoftLayer_Product_Package_Server']

objectFilter = {"packageType": {"operation": "in", "options":
    [{"name": "data", "value": ["BARE_METAL_CPU_FAST_PROVISION"]}]}}

try:
    servers = packageService.getAllObjects(filter=objectFilter)
    print(json.dumps(servers, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to list the servers to order. \nfaultCode= %s, \nfaultString= %s"
          % (e.faultCode, e.faultString))

```
