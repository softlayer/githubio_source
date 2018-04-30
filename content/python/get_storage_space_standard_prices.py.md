---
title: "get_storage_space_standard_prices.py"
description: "get_storage_space_standard_prices.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Product_Package"
tags:
    - "endurance"
---


```
"""
Get the storage space prices to order an endurance space.

The script retrieves all the storage spaces prices which
meet an IOPS requirement and these prices are standard
prices (they work for any datacenter).

Important manual pages:
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

# value = 200 is for 2 IOPS per GB.
# value = 100 is for 0.25 IOPS per GB.
# value = 300 is for 4 IOPS per GB.
iops = 100

# Declares the API client
client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
productPackage = client['SoftLayer_Product_Package']

# Declares an object filter in order to get only the standard prices
# which are for storage spaces and meet the requirements for
# the configured IOPS.
objectFilter = {"items": {"prices": {"capacityRestrictionMaximum": {"operation": iops}, "categories": {"categoryCode": {"operation": "performance_storage_space"}}, "locationGroupId": {"operation": "is null"}}}}

try:
    items = productPackage.getItems(id=packageId, filter=objectFilter)
    print(json.dumps(items, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to get the prices. faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))

```
