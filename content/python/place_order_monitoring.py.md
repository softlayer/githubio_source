---
title: "place_order_monitoring.py"
description: "place_order_monitoring.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Product_Order"
    - "SoftLayer_Container_Product_Order_Monitoring_Package"
    - "SoftLayer_Monitoring_Agent_Configuration_Template_Group"
tags:
    - "monitoring"
---


```
"""
Order a Monitoring Package

Build a SoftLayer_Container_Product_Order_Monitoring_Package object for a new
monitoring order and pass it to the SoftLayer_Product_Order API service to order it
In this care we'll order a Basic (Hardware and OS) package with Basic Monitoring Package - Linux
configuration for more details see below

Important manual pages:
https://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order_Monitoring_Package
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Item_Price
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/verifyOrder
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Monitoring_Agent_Configuration_Template_Group

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer

USERNAME = 'set me'
API_KEY = 'set me'

"""
Build a skeleton SoftLayer_Container_Product_Order_Monitoring_Package object
containing the order you wish to place.
"""
oderTemplate = {
    'complexType': 'SoftLayer_Container_Product_Order_Monitoring_Package',
    'packageId': 0,  # the packageID for order monitoring packages is 0
    'prices': [
        {'id': 2302}  # this is the price for Monitoring Package - Basic ((Hardware and OS))
    ],
    'quantity': 0,  # the quantity for order a service (in this case monitoring package) must be 0
    'sendQuoteEmailFlag': True,
    'useHourlyPricing': True,
    'virtualGuests': [
        {'id': 4906034}  # the virtual guest ID where you want add the monitoring package
    ],
    'configurationTemplateGroups': [
        {'id': 3}  # the templateID for the monitoring group (in this case Basic Monitoring package for Unix/Linux operating system.)
    ]
}

# Declare the API client to use the SoftLayer_Product_Order API service
client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
productOrderService = client['SoftLayer_Product_Order']

"""
verifyOrder() will check your order for errors. Replace this with a call to
placeOrder() when you're ready to order. Both calls return a receipt object
that you can use for your records.

Once your order is placed it'll go through SoftLayer's provisioning process.
"""
try:
    order = productOrderService.verifyOrder(oderTemplate)
    print(order)
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to verify the order! faultCode=%s, faultString=%s"
          % (e.faultCode, e.faultString))
    exit(1)

```
