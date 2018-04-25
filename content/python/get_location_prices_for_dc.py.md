---
title: "get_location_prices_for_dc.py"
description: "get_location_prices_for_dc.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Product_Package"
tags:
    - "package"
---


```
"""
Get location prices for a datacenter

This script retrieves location prices for a package from a specific datacenter

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Package/getItemPrices
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Item_Price
http://sldn.softlayer.com/article/Object-Filters
@License: http://sldn.softlayer.com/article/License
@Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

# So we can talk to the SoftLayer API:
import SoftLayer
import json

# Your SoftLayer API username and key.
API_USERNAME = 'set me'
API_KEY = 'set me'
# Declare the package id
packageId = 265
# Declare the datacenter name that you wish to retrieve the item prices
datacenter = 'London 1'
# Create a client instance
client = SoftLayer.Client(username=API_USERNAME, api_key=API_KEY)
objectMask = 'mask[pricingLocationGroup[locations[longName]]]'
# Declare an object filter to get location item prices
objectFilter = {'itemPrices': {'pricingLocationGroup': {'locations': {'longName': {'operation': datacenter}}}}}
try:
    standardPrices = client['SoftLayer_Product_Package'].getItemPrices(id=packageId, mask=objectMask, filter=objectFilter)
    print(json.dumps(standardPrices, sort_keys=True, indent=2, separators=(',', ':')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to get location item prices faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))
    exit(1)

```
