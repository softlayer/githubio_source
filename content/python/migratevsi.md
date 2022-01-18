---
title: "Migrating a VSI from SAN to Local Storage and vice-versa"
description: "Example on how to call verifyOrder / placeOrder via REST to migrate a Virtual_Guest from SAN to Local storage and vice-versa."
date: "2016-11-07"
classes: ["SoftLayer_Product_Order"]
tags:
    - "placeorder"
    - "verifyorder"
    - "upgrade"
---

You can use the following [python example](https://softlayer.github.io/python/list_packages/) to get a list of all the available priceId's for the Virtual_Guest package. You need to change the second to last line from main.getPackage(126) to main.getPackage(46). The priceId you need will depend on if you are moving to or from Local Storage and the size of the current primary drive.

```python

import SoftLayer
import json

# The package for Virtual Guests
packageId = 46

# Our exising VSI ID
virtualGuests = [
    {
        "id":25367125
    }
]

# The price item id for a 25GB Local Primary Drive.
prices = [
   {
     "id":13899,
     "categories":[
        {
            "categoryCode":"guest_disk0",
            "id":81,
            "name":"First Disk"
        }
    ]
   }
]

# Maintenance Window time. The migration requires downtime
properties = [
    {
        "name":"MAINTENANCE_WINDOW",
        "value":"now"
    }
]

# Declare the API client.
client = SoftLayer.Client()
productOrderService = client['SoftLayer_Product_Order']

# The parameters needed for the migration order
orderData = {
   "complexType": "SoftLayer_Container_Product_Order_Virtual_Guest_Upgrade",
   "packageId": packageId,
   "prices": prices,
   "properties": properties,
   "virtualGuests" : virtualGuests,
}

try:
   # verifyOrder() will check your order for errors. Replace this with a call to
   # placeOrder() when you're ready to order. Both calls return a receipt object
   # that you can use for your records.
   response = productOrderService.verifyOrder(orderData)
   print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
   # If there was an error returned from the SoftLayer API then bomb out with the
   # error message.
   print("Unable to place the order. faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))


```
