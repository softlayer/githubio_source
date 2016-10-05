---
title: "Required the available servers to order"
date: "2016-01-11"
classes: ["SoftLayer_Product_Package_Server"]
tags:
  - "ordering"
  - "Bare Metal"
---

```python
"""
List all the vailable servers to order.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Package_Server/getAllObjects
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Package_Server/
http://sldn.softlayer.com/article/Object-Filters

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer
import json

client = SoftLayer.Client()
packageService = client['SoftLayer_Product_Package_Server']

objectFilter = {
    "packageType": {
        "operation": "in",
        "options": [{
            "name": "data",
            "value": [
                "BARE_METAL_CORE",
                "BARE_METAL_CPU",
                "BARE_METAL_CPU_FAST_PROVISION"
            ]
        }]
    }
}

try:
    servers = packageService.getAllObjects(filter=objectFilter)
    print(json.dumps(servers, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to list the servers to order. faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))

```