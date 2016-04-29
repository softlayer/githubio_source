---
title: "Order a Local Load Balancer"
description: "Order a local load balancer using SoftLayer_Product_Item_Price objects"
date: "2016-04-29"
classes: ["SoftLayer_Product_Order"]
tags:
    - "placeOrder"
    - "verifyOrder"
---


```python
"""
Order a load balancer

Important manual pages:
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Item_Price
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/verifyOrder
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer
import json


# The package to order load balancers.
packageId = 194

# Build a skeleton SoftLayer_Product_Item_Price objects. These objects contain
# much more than ids, but SoftLayer's ordering system only needs the price's id
# to know what you want to order.

# Since Load Balancers can have Location Specific itemPriceId's I am using the following script to
# return just the standard (location agnostic) itemPriceId's.
# https://gist.github.com/greyhoundforty/a0b55afcab9bc758405e21a39b93c63d
# In my case I am going with 'Load Balancer 500 VIP Connections'

prices = [
   {
       "id": 2078
   }
]

# Declare the API client.
client = SoftLayer.Client()
productOrderService = client['SoftLayer_Product_Order']

orderData = {
   "prices": prices,
   "packageId": packageId,
   "location": "DALLAS06"
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
