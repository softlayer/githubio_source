---
title: "Location-based Pricing and You"
description: "When we launch a new data center, we try to keep everything as consistent as possible between locations. We use the same"
date: "2015-07-22"
author: "cmporter"
tags:
    - "blog"
---

When we launch a new data center, we try to keep everything as consistent as possible between locations. We use the same hardware, we have a skilled “Go Live” team to bring everything online, and we train our local operations staff the same way. When we open a new data center in Dallas, that’s easy. But when the new facility is on the other side of the planet, things can get a little more complicated.

In addition to the costs we incur to ship hardware across oceans, we encounter significant variations in  service costs from one location to the next. In the past, we accounted for these cost variations by adding premiums to servers and services when they were ordered, but those premiums were somewhat confusing; one location may have a fixed dollar amount premium while another had a percentage premium based on the total cost. 

To simplify the ordering process, we updated our pricing model to represent the costs in each data center more clearly. Instead of adding premiums to a base server price, we have priced servers and services in each data center with their own location-based [<code>SoftLayer_Product_Item_Price</code>](http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Item_Price) objects via the API.

## **The data model**
The changes made to the pricing model facilitated some new properties and relations on objects represented in the API.

On [<code>SoftLayer_Product_Item_Price</code>](http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Item_Price), a new property <code>locationGroupId</code> and relation <code>pricingLocationGroup</code> were added. The pricing location group refers to the [<code>SoftLayer_Location_Group_Pricing</code>](http://sldn.softlayer.com/reference/datatypes/SoftLayer_Location_Group_Pricing) object of which the price is a member.

If a price has <code>locationGroupId</code> and <code>pricingLocationGroup</code> set to null, this means that the price is a standard price and can be used when ordering for any location. If a price has <code>locationGroupId</code> and <code>pricingLocationGroup</code> set, then this means that the price is a location-based price. When ordering, the price can only be used in a datacenter that is in the locations on the [<code>SoftLayer_Location_Group_Pricing</code>](http://sldn.softlayer.com/reference/datatypes/SoftLayer_Location_Group_Pricing) object.

The new [<code>SoftLayer_Location_Group_Pricing</code>](http://sldn.softlayer.com/reference/datatypes/SoftLayer_Location_Group_Pricing) type represents a set of prices that can only be used in a set of locations. The pricing location group has the following relations:

- prices to [<code>SoftLayer_Product_Item_Price</code>](http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Item_Price) objects.
- locations to [<code>SoftLayer_Location</code>](http://sldn.softlayer.com/reference/datatypes/SoftLayer_Location) objects.

On [<code>SoftLayer_Location</code>](http://sldn.softlayer.com/reference/datatypes/SoftLayer_Location), a new relation was added, <code>priceGroups</code>, which refers to [<code>SoftLayer_Location_Group_Pricing</code>](http://sldn.softlayer.com/reference/datatypes/SoftLayer_Location_Group_Pricing) objects, if the location has any. Some data centers use standard pricing only, so this relation would be empty for them.

## **Standard price replacement when ordering**
A standard price will be replaced on an [order container](http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order) when [<code>SoftLayer_Product_Order::verifyOrder</code>](http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/verifyOrder) or [<code>SoftLayer_Product_Order::placeOrder</code>](http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder) are called if there is a location-based price that exists for the data center being ordered into for the same [item](http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Item).

It is recommended to first use [<code>SoftLayer_Product_Order::verifyOrder</code>](http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/verifyOrder) and check if prices have been replaced. The fees associated with the order may change because of the replacement being performed, so make sure you are aware of those changes before you call [<code>SoftLayer_Product_Order::placeOrder</code>](http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder).

## **Usage**
When querying the API for anything that includes [prices](http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Item_Price), they may be location-based. If you’re only interested in pricing for a specific data center, you should consider filtering by the location group on the resultant prices or use object filters. 

## **Examples**
Let's take a simple example. Here we have a basic query to the items and prices on the virtual server package with the following script:

```
import SoftLayer
import json

client = SoftLayer.create_client_from_env(username="USERNAME", api_key="API_KEY")
items = client["SoftLayer_Product_Package"].getItems(id=46)

print(json.dumps(items, sort_keys=True, indent=2, separators=(',', ': ')))
```

will output a number of records similar to:

```
[
  {
    "capacity": "16",
    "description": "16 GB ",
    "id": 1017,
    "itemTaxCategoryId": 166,
    "keyName": "RAM_16_GB",
    "prices": [
      {
        "currentPriceFlag": "",
        "hourlyRecurringFee": ".211",
        "id": 1927,
        "itemId": 1017,
        "laborFee": "0",
        "locationGroupId": "",
        "onSaleFlag": "",
        "oneTimeFee": "0",
        "quantity": "",
        "recurringFee": "140",
        "setupFee": "0",
        "sort": 0
      },
      {
        "currentPriceFlag": "",
        "hourlyRecurringFee": ".238",
        "id": 51525,
        "itemId": 1017,
        "laborFee": "0",
        "locationGroupId": 509,
        "onSaleFlag": "",
        "oneTimeFee": "0",
        "quantity": "",
        "recurringFee": "158",
        "setupFee": "0",
        "sort": 0
      },
      {
        "currentPriceFlag": "",
        "hourlyRecurringFee": ".253",
        "id": 51531,
        "itemId": 1017,
        "laborFee": "0",
        "locationGroupId": 545,
        "onSaleFlag": "",
        "oneTimeFee": "0",
        "quantity": "",
        "recurringFee": "168",
        "setupFee": "0",
        "sort": 0
      },
      ...
    ],
    "softwareDescriptionId": "",
    "units": "GB",
    "upgradeItemId": ""
  },
  ...
]
```

Looking at this result, you'll see that we have prices that are standard because their <code>locationGroupId</code> is empty. You'll also see we have location-based prices because their locationGroupId refers to a specific [<code>SoftLayer_Location_Group_Pricing</code>](http://sldn.softlayer.com/reference/datatypes/SoftLayer_Location_Group_Pricing) object. 

If we wanted to filter our results to only include standard pricing, we can use object filters with any client that supports them to do this:

```
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

client = SoftLayer.create_client_from_env(username="USERNAME", api_key="API_KEY")
items = client["SoftLayer_Product_Package"].getItems(id=46, filter=object_filter)

print(json.dumps(items, sort_keys=True, indent=2, separators=(',', ': ')))
```


Now our items only include standard prices, which are ones where the <code>locationGroupId</code> is null. This is the simplest way to handle location-based prices as mentioned above because the order process will figure out the location-based prices for you when you verify or place your order. 

Let's say we know in advance which data center we want to order a server in, so we want to query for the prices that we can use. We can query for the data center, and then filter our items and prices to include only the location-based pricing for the specific data center we're in —or we can filter for the standard price if a location-based price doesn't exist:

```
import SoftLayer
import json

package_id = 46
datacenter = 'tor01'

client = SoftLayer.create_client_from_env(username="USERNAME", api_key="API_KEY")

location_object_filter = {
    'name': {'operation': datacenter}
}

location_object_mask = "priceGroups"

location = client["SoftLayer_Location_Datacenter"].getDatacenters(filter=location_object_filter, mask=location_object_mask)

if len(location) == 0:
    # error handling
    exit()
```

# lookup location group ids

```
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
```

# let's key by item id

```python
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

This will filter down the prices on the items and return a dictionary keyed by item. We could key by any other property, or sort by category code and directly choose the prices we want on the order for each.

-Cameron

