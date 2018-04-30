---
title: "order_consistent_performance_storage_nfs.py"
description: "order_consistent_performance_storage_nfs.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Product_Order"
    - "SoftLayer_Container_Product_Order_Network_PerformanceStorage_Nfs"
tags:
    - "iscsi"
---


```
"""
Order Consistent Performance Storage Nfs.

This script creates an order for Consistent Performance Storage Nfs (Monthly)

See below references for more details.
Important manual pages:
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

# Create a client instance
client = SoftLayer.Client(username=API_USERNAME, api_key=API_KEY)
orderTemplate = {
    'complexType': 'SoftLayer_Container_Product_Order_Network_PerformanceStorage_Nfs',
    'quantity': 1,
    'packageId': 222,
    'location': 'DALLAS09',
    'prices': [
        {'id': 40662},  # Block Storage (Consistent Performance)
        {'id': 40682},  # 20 GB Storage Space
        {'id': 40792}  # Consistent Performance Storage IOPS
    ]
}
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
    print("Error cannot verify the order  faultCode=%s, faultString=%s"
          % (e.faultCode, e.faultString))
    exit(1)

```
