---
title: "create_standard_firewall.py"
description: "create_standard_firewall.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Product_Package"
    - "SoftLayer_Product_Order"
    - "SoftLayer_Container_Product_Order_Network_Protection_Firewall"
tags:
    - "firewalls"
---


```
#
# Create a standard firewall
#
# This script will config a firewall service on
# a virtual instance using the SoftLayer_Product_Order::placeOrder
# method it is needed to build a skeleton of a virtual guest
# object and provide the ID of virtual instance in which
# the firewall service will be configured
# To get prices IDs for firewall service use
# SoftLayer_Product_Package::getCategories method.
#
# Important manual pages:
# http://sldn.softlayer.com/reference/services/SoftLayer_Product_Package/placeOrder
# http://sldn.softlayer.com/reference/services/SoftLayer_Product_Package/getCategories
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order_Network_Protection_Firewall
# @License: http://sldn.softlayer.com/article/License
# @Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>

# So we can talk to the SoftLayer API:
import SoftLayer
# For nice debug output
import pprint

# Your SoftLayer API username and key.
#
# Generate an API key at the SoftLayer Customer Portal

API_USERNAME = 'set-me'
API_KEY = 'set-me'

serverId = 8755943

orderTemplate = {
    'complexType': 'SoftLayer_Container_Product_Order_Network_Protection_Firewall',
    'packageId': 0,
    'quantity': 1,
    'virtualGuests': [
        {'id': serverId}
    ],
    'prices': [
        {'id': 409}
    ]
}
# Create a client object.
client = SoftLayer.Client(username=API_USERNAME, api_key=API_KEY)
# Replace the verifyOrder() method with placeOrder
# after testing.
try:
    result = client['Product_Order'].verifyOrder(orderTemplate)
    pprint.pprint(result)
except SoftLayer.SoftLayerAPIError as e:
    print("Error  faultCode=%s, faultString=%s"
          % (e.faultCode, e.faultString))
    exit(1)

```
