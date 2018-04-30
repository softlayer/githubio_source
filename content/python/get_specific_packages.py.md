---
title: "get_specific_packages.py"
description: "get_specific_packages.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Product_Package_Server"
tags:
    - "package"
---


```
"""
Get specific packages

The script displays all the packages which contains
a determinate  kind of processor.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Package_Server
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Package_Server/getAllObjects

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
import SoftLayer

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'

# The filter to find determinate processors in the result
# and only retrieve those processors from the API
objectFilter = {"processorName": {"operation": "in", "options": [{"name": "data", "value": ["Xeon 2650", "Xeon 5650"]}, ]}}

# Declare the API client
client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
packageServerService = client['SoftLayer_Product_Package_Server']

try:
    result = packageServerService.getAllObjects(filter=objectFilter)
    print(result)
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to retrieve the packages faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))
    exit(1)

```
