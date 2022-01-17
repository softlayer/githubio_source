---
title: "Find Location specific pricing for a package"
description: "Use an object filter and object mask to return the Location Based pricing information for a SoftLayer package."
date: "2016-04-12"
classes: ["SoftLayer_Product_Package"]
tags:
    - "objectfilter"
    - "objectmask"
    - "pricing"
---

With the introduction to Location-based Pricing, we updated our pricing model to represent the costs in each data center more clearly. Instead of adding premiums to a base server price, we have priced servers and services in each data center with their own location-based [SoftLayer_Product_Item_Price](http://sldn.softlayer.com/reference/services/SoftLayer_Product_Item_Price) objects via the API. In the following example we will query for the Dallas 6 data center, and then filter our item (Local Load Balancer) and prices to include only the location-based pricing for the specific data center we're in —or we can filter for the standard price if a location-based price doesn't exist. 

```python

import SoftLayer
import json

package_id = 194
datacenter = 'dal06'

client = SoftLayer.Client()

location_object_filter = {
    'name': {'operation': datacenter}
}

location_object_mask = "priceGroups"

location = client["SoftLayer_Location_Datacenter"].getDatacenters(filter=location_object_filter, mask=location_object_mask)

if len(location) == 0:
    # error handling
    exit()

# lookup location group ids
location_group_ids = []
for location_group in location[0]["priceGroups"]:
    location_group_ids.append(location_group["id"])

object_filter_standard = {
    'items': {
        "prices": {
            "locationGroupId": {
                "operation": "is null"
            }
        }
    }
}

standard_items = client["SoftLayer_Product_Package"].getItems(id=package_id, filter=object_filter_standard)

object_filter_location = {
    'items': {
        "prices": {
            "locationGroupId": {
                "operation": "in",
                "options": [
                    {
                        "name": "data",
                        "value": location_group_ids
                    }
                ]
            }
        }
    }
}

location_items = client["SoftLayer_Product_Package"].getItems(id=package_id, filter=object_filter_location)

# let's key by item id
items = {}

for standard_item in standard_items:
    for location_item in location_items:
        if location_item["id"] == standard_item["id"]:
            items[location_item["id"]] = location_item
            break

    if standard_item["id"] not in items:
        items[standard_item["id"]] = standard_item


print(json.dumps(items, sort_keys=True, indent=2, separators=(',', ': ')))


```