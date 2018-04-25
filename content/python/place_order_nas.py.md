---
title: "place_order_nas.py"
description: "place_order_nas.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Container_Product_Order_Network_Storage_Nas"
    - "SoftLayer_Product_Order"
tags:
    - "nas"
---


```
"""
Order a NAS

Build a SoftLayer_Container_Product_Order_Network_Storage_Nas
object for a new CDN account order and pass it to the SoftLayer_Product_Order
API service to order it. In this script we'll order a NAS. See below for more details.

Important manual pages:
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order_Network_Storage_Nas
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Item_Price
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/verifyOrder
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
import SoftLayer

USERNAME = 'set me'
# Generate one at https://manage.softlayer.com/Administrative/apiKeychain
API_KEY = 'set me'

"""
Build a skeleton SoftLayer_Container_Product_Order_Network_Storage_Nas object
containing the order you wish to place.
"""
orderData = {
    "complexType": "SoftLayer_Container_Product_Order_Network_Storage_Nas",
    "packageId": 216,  # the package id to order NAS
    "location": "AMSTERDAM",
    # The prices to order the NAS
    "prices": [
        {
            "complexType": "SoftLayer_Product_Item_Price",
            "id": 508  # 20 GB NAS
        }

    ],
    "quantity": 1,
    "privateCloudOrderFlag": False
}

# Declare the API client
client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
productOrderService = client['SoftLayer_Product_Order']

try:
    """
    verifyOrder() will check your order for errors. Replace this with a call to
    placeOrder() when you're ready to order. Both calls return a receipt object
    that you can use for your records.
    """
    response = client['SoftLayer_Product_Order'].verifyOrder(orderData)
    print(response)
except SoftLayer.SoftLayerAPIError as e:
    # If there was an error returned from the SoftLayer API then bomb out with the
    # error message.
    print("Unable to place order faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))

```
