---
title: "place_order_cdn.py"
description: "place_order_cdn.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Network_ContentDelivery_Account"
    - "SoftLayer_Product_Order"
    - "SoftLayer_Container_Product_Order_Network_ContentDelivery_Account"
tags:
    - "cdn"
---


```
"""
Order a new CDN account

Build a SoftLayer_Container_Product_Order_Network_ContentDelivery_Account
object for a new CDN account order and pass it to the SoftLayer_Product_Order
API service to order it. In this case we'll order a pay as you go bandwidth
and storage CDN account. See below for more details.

Important manual pages:
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order_Network_ContentDelivery_Account
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_ContentDelivery_Account
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Item_Price
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Order/verifyOrder
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Order/placeOrder

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
import SoftLayer

USERNAME = 'set me'
API_KEY = 'set me'

"""
Build a skeleton SoftLayer_Container_Product_Order_Network_ContentDelivery_Account object
containing the order you wish to place.
"""
orderData = {
    "complexType": "SoftLayer_Container_Product_Order_Network_ContentDelivery_Account",

    "packageId": 208,  # The package id to order Content Delivery Network
    # The prices to order the CDN
    "prices": [
        {
            "complexType": "SoftLayer_Product_Item_Price",
            "id": 1661  # CDN Pay as You Go Bandwidth
        },

        {
            "complexType": "SoftLayer_Product_Item_Price",
            "id": 1670  # CDN No storage (origin pull)
        }
    ],
    "quantity": 1,  # We only want 1 fire-wall
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
    """
    If there was an error returned from the SoftLayer API then bomb out with the
    error message.
    """
    print("Unable to place order faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))

```
