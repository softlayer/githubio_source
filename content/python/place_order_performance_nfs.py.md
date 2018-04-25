---
title: "place_order_performance_nfs.py"
description: "place_order_performance_nfs.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Container_Product_Order"
    - "SoftLayer_Product_Order"
    - "SoftLayer_Product_Package"
tags:
    - "performancenfs"
---


```
"""
Order performance NFS storage.

The script orders a performance NFS storage with 40GB storage space
and 100 IOPS. It makes a single call to SoftLayer_Product_Order::placeOrder method.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Item_Price
"""
import SoftLayer

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'

# Building an skeleton SoftLayer_Container_Product_Order for the order
orderTemplate = {
    "complexType": "SoftLayer_Container_Product_Order",
    "location": "DALLAS05",
    # The package for order performance NFS storage.
    "packageId": 222,
    # The prices for the performance NFS storage
    # To see the list of prices available for the package
    # use the Softlayer_Product_Package::getItems method (http://sldn.softlayer.com/reference/services/SoftLayer_Product_Package/getItems)
    # e.g.
    # client = SoftLayer::Client.new(:username => user,:api_key => api_key)
    # productPackageService = client.service_named("Softlayer_Product_Package")
    # packageID = 222
    # result = productPackageService.object_with_id(packageID).getItems()
    "prices": [
        {
            "id": 40662  # performance storage nfs.
        },
        {
            "id": 40692  # 40GB Storage Space.
        },
        {
            "id": 40892  # 100 IOPS.
        }
    ]
}

# Declares the API client to use the SoftLayer_Product_Order API service
client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
productOrderService = client['SoftLayer_Product_Order']

try:
    # Verifies the order when you are ready to create the
    # performance NFS storage replace "verifyOrder" by "placeOrder"
    result = productOrderService.verifyOrder(orderTemplate)
    print(result)
except SoftLayer.SoftLayerAPIError as e:
    # If there was an error returned from the SoftLayer API then bomb out with the
    # error message.
    print("Unable to place the order. "
          % (e.faultCode, e.faultString))

```
