---
title: "place_order_block_storage.py"
description: "place_order_block_storage.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Storage_Iscsi_"
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Product_Package"
    - "SoftLayer_Product_Order"
    - "SoftLayer_Container_Product_Order_Network_PerformanceStorage_Iscsi"
tags:
    - "blockstorage"
---


```
"""
Order a block storage (performance)

The script orders a block storage (performance) device,
with 40GB storage and 600 IOPS, it makes a single call to
SoftLayer_Product_Order::placeOrder method.

Important manual pages:
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order_Network_PerformanceStorage_Iscsi
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Item_Price
"""
import SoftLayer

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'

# Building an skeleton SoftLayer_Container_Product_Order_Network_PerformanceStorage_Iscsi to the order
orderTemplate = {
    "complexType": "SoftLayer_Container_Product_Order_Network_PerformanceStorage_Iscsi",
    "location": "DALLAS05",
    "quantity": 1,
    # The package for order block storage
    "packageId": 222,
    # The prices for the block storage, it required you specify
    # a storage space and IOPS in the template.
    # To see the list of prices available for the package
    # use the Softlayer_Product_Package::getItems method (http://sldn.softlayer.com/reference/services/SoftLayer_Product_Package/getItems)
    # e.g.
    # client = SoftLayer::Client.new(:username => user,:api_key => api_key)
    # productPackageService = client.service_named("Softlayer_Product_Package")
    # packageID = 222
    # result = productPackageService.object_with_id(packageID).getItems()
    "prices": [
        {
            "id": 40672  # BlockStorage(Performance)
        },
        {
            "id": 40692  # 40GB Storage Space
        },
        {
            "id": 40942  # 600 IOPS
        }
    ],
    "osFormatType": {
        "keyName": "LINUX",
        "complexType": "SoftLayer_Network_Storage_Iscsi_OS_Type"
    }
}

# Declares the API client to use the SoftLayer_Product_Order API service
client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
productOrderService = client['SoftLayer_Product_Order']

try:
    # Verifies the order when you are ready to create the
    # block storage replace "verifyOrder" by "placeOrder"
    result = productOrderService.verifyOrder(orderTemplate)
    print(result)
except SoftLayer.SoftLayerAPIError as e:
    # If there was an error returned from the SoftLayer API then bomb out with the
    # error message.
    print("Unable to place the order. "
          % (e.faultCode, e.faultString))

```
