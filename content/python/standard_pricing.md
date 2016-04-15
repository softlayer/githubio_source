---
title: "Find standard location pricing for a package"
description: "Use an object filter to only return the Standard Location pricing for a SoftLayer package. This is a priceItemId that is standard accross all SoftLayer Datacenters"
date: "2016-04-12"
classes: ["SoftLayer_Product_Package"]
tags:
    - "object_filter"
    - "pricing"
---

With the introduction to Location-based Pricing, we updated our pricing model to represent the costs in each data center more clearly. Instead of adding premiums to a base server price, we have priced servers and services in each data center with their own location-based [SoftLayer_Product_Item_Price](http://sldn.softlayer.com/reference/services/SoftLayer_Product_Item_Price) objects via the API. The following example shows how to get the Standard priceItemId for a package regardless of the location. 

```python

import SoftLayer
import json

object_filter = {
    'items': {
        'prices': {
            'locationGroupId': {
                'operation': 'is null'
            }
        }
    }
}

client = SoftLayer.Client()
items = client["SoftLayer_Product_Package"].getItems(id=194, filter=object_filter)

print(json.dumps(items, sort_keys=True, indent=2, separators=(',', ': ')))

```

