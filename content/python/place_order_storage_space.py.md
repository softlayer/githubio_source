---
title: "place_order_storage_space.py"
description: "place_order_storage_space.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Product_Order"
    - "SoftLayer_Container_Product_Order_Network_Storage_Enterprise_SnapshotSpace"
tags:
    - "endurance"
---


```
"""
Order storage space.

The script adds an storage space of 10 GB to an endurance storage.

Important manual pages:
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order_Network_Storage_Enterprise_SnapshotSpace
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Item_Price
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/verifyOrder
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer

USERNAME = 'set me'
API_KEY = 'set me'


# Build a skeleton SoftLayer_Container_Product_Order_Network_Storage_Enterprise_SnapshotSpace object
# containing the order you wish to place.
orderData = {
    "complexType": "SoftLayer_Container_Product_Order_Network_Storage_Enterprise_SnapshotSpace",
    "volumeId": 6538873,  # The storage endurance id where you wish to add the storage space.
    "packageId": 240,
    "quantity": 1,
    "prices": [
        {
            "id": 46150  # 10 GB Storage Space.
        }
    ]
}

# Declares the API client
client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
productOrderService = client['SoftLayer_Product_Order']

try:
    # verifyOrder() will check your order for errors. Replace this with a call to
    # placeOrder() when you're ready to order. Both calls return a receipt object
    # that you can use for your records.
    response = productOrderService.verifyOrder(orderData)
    print(response)
except SoftLayer.SoftLayerAPIError as e:
    # If there was an error returned from the SoftLayer API then bomb out with the
    # error message.
    print("Unable to place the order. faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))

```
