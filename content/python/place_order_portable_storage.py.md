---
title: "place_order_portable_storage.py"
description: "place_order_portable_storage.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Container_Product_Order_Virtual_Disk_Image"
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Product_Package"
    - "SoftLayer_Product_Order"
tags:
    - "portablestorage"
---


```
"""
Order a portal storage

The script orders a portal storage device, it makes a single call to
SoftLayer_Product_Order::placeOrder method.

Important manual pages:
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order_Virtual_Disk_Image
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Item_Price
"""
import SoftLayer

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'

# Declare the API client to use the SoftLayer_Product_Order API service
client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
productOrderService = client['SoftLayer_Product_Order']

# Building an skeleton SoftLayer_Container_Product_Order_Virtual_Disk_Image to the order
orderTemplate = {
    "complexType": "SoftLayer_Container_Product_Order_Virtual_Disk_Image",
    "location": "SANJOSE",
    # The package for order portable storage
    "packageId": 198,
    "diskDescription": "test portable storage",
    "prices": [
        {
            # The prices for the portable storage
            # to see the list of prices available for the package
            # use the Softlayer_Product_Package::getItems method (http://sldn.softlayer.com/reference/services/SoftLayer_Product_Package/getItems)
            # e.g.
            # client = SoftLayer::Client.new(:username => user,:api_key => api_key)
            # productPackageService = client.service_named("Softlayer_Product_Package")
            # packageID = 198
            # result = productPackageService.object_with_id(packageID).getItems()
            "id": 21861,
            "complexType": "SoftLayer_Product_Item_Price"
        }
    ]
}

try:
    # Verifies the order when you are ready to create the
    # portal storage replace "verifyOrder" by "placeOrder"
    result = productOrderService.verifyOrder(orderTemplate)
    print(result)
except SoftLayer.SoftLayerAPIError as e:
    # If there was an error returned from the SoftLayer API then bomb out with the
    # error message.
    print("Unable to place the order. "
          % (e.faultCode, e.faultString))

```
