---
title: "get_standard_prices.py"
description: "get_standard_prices.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Product_Package"
tags:
    - "package"
---


```
"""
Get standard prices

This script retrieves standard prices for an package

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
# Create a client instance
client = SoftLayer.Client(username=API_USERNAME, api_key=API_KEY)
# Declare an object filter to get standard item prices
objectFilter = {'itemPrices': {'locationGroupId': {'operation': 'is null'}}}
try:
    standardPrices = client['SoftLayer_Product_Package'].getItemPrices(id=packageId, filter=objectFilter)
    print(json.dumps(standardPrices, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to get standard item prices faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))
    exit(1)

```
