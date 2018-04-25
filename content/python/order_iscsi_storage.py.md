---
title: "order_iscsi_storage.py"
description: "order_iscsi_storage.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Product_Order"
    - "SoftLayer_Container_Product_Order_Network_Storage_Iscsi"
tags:
    - "iscsi"
---


```
"""
Order iSCSI Storage.

This script creates an order for iSCSI Storage (Monthly)

See below references for more details.
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder/
@License: http://sldn.softlayer.com/article/License
@Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
# So we can talk to the SoftLayer API:
import SoftLayer

# For nice debug output:
import pprint

# Your SoftLayer API username and key.
API_USERNAME = 'set-me'
API_KEY = 'set-me'

orderTemplate = {
    'complexType': 'SoftLayer_Container_Product_Order_Network_Storage_Iscsi',
    'quantity': 1,
    'packageId': 218,
    'location': 'DALLAS07',
    'prices': [
        {'id': 1033}  # 20 GB iSCSI SAN Storage
    ]
}
# Create a client instance
client = SoftLayer.Client(username=API_USERNAME, api_key=API_KEY)
"""
Verify the order container is right. If this returns an error
then fix your order container and re-submit. Once ready then place
your order with the placeOrder() method.
"""
try:
    result = client['Product_Order'].verifyOrder(orderTemplate)
    print("Order verified")
    pprint.pprint(result)
except SoftLayer.SoftLayerAPIError as e:
    print("Error cannot verified the order  faultCode=%s, faultString=%s"
          % (e.faultCode, e.faultString))
    exit(1)

```
