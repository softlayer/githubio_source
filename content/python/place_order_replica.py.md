---
title: "place_order_replica.py"
description: "place_order_replica.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Container_Product_Order_Network_Storage_Enterprise"
    - "SoftLayer_Product_Order"
    - "SoftLayer_Network_Storage"
tags:
    - "endurance"
---


```
"""
Order snapshot replica.

Build a SoftLayer_Container_Product_Order_Network_Storage_Enterprise
object to order a replica for your endurance object storage.

Important manual pages:
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order_Network_Storage_Enterprise
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Item_Price
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/verifyOrder
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer

USERNAME = 'set me'
API_KEY = 'set me'

# Builds a skeleton SoftLayer_Container_Product_Order_Network_Storage_Enterprise object
# containing the order you wish to place.
orderData = {
    "complexType": "SoftLayer_Container_Product_Order_Network_Storage_Enterprise",
    "packageId": 240,
    # In order to get the valid locations for the replica
    # call the SoftLayer_Network_Storage::getValidReplicationTargetDatacenterLocations method
    # e.g.
    # client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
    # enduranceStorage = 6548079
    # storageService = client['SoftLayer_Network_Storage']
    # result = storageService.getValidReplicationTargetDatacenterLocations(id=enduranceStorage)
    # print(result)
    "location": "AMSTERDAM03",
    "originVolumeId": 6548079,  # The storage endurance id where you wish to create the replica.
    # This is the origin volume schedule, you can get this id by calling SoftLayer_Network_Storage::getSchedules
    # client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
    # enduranceStorage = 6548079
    # storageService = client['SoftLayer_Network_Storage']
    # result = storageService.getSchedules(id=enduranceStorage)
    # print(result)
    "originVolumeScheduleId": 34247,
    "quantity": 1,
    "prices": [
        {
            "id": 46649  # 20 GB Storage Space (Replication)
        },
        {
            "id": 45098  # Block Storage
        },
        {
            "id": 45068  # 0.25 IOPS per GB
        },
        {
            "id": 144005  # 20 GB Storage Space
        },
        {
            "id": 144255  # 5 GB Storage Space
        },
        {
            "id": 45058  # Endurance Storage
        }
    ],
    "osFormatType": {
        "keyName": "LINUX"
    }
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
    print("Unable to place the order faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))

```
