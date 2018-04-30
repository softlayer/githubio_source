---
title: "get_iops_standard_price.py"
description: "get_iops_standard_price.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Product_Item"
    - "SoftLayer_Product_Package"
tags:
    - "endurance"
---


```
"""
Get IOPS prices to order a endurance object storage.

Important manual pages:
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Package
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Item
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Package
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Package/getItems

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
import SoftLayer
import json

USERNAME = 'set me'
API_KEY = 'set me'

# The package id to order endurance object storage.
packageId = 240

client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
productPackage = client['SoftLayer_Product_Package']

# A filter to get only the prices for IOPS.
objectFilter = {"items": {"prices": {"categories": {"categoryCode": {"operation": "storage_tier_level"}}, "locationGroupId": {"operation": "is null"}}}}

try:
    items = productPackage.getItems(id=packageId, filter=objectFilter)
    print(json.dumps(items, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to get the prices. faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))

```
