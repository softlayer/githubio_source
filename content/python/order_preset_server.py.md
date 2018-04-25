---
title: "order_preset_server.py"
description: "order_preset_server.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Container_Product_Order"
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Product_Order"
    - "SoftLayer_Container_Product_Order_Hardware_Server"
    - "SoftLayer_Hardware_Server"
tags:
    - "baremetalservers"
---


```
"""
Order a new server with preset configuration.

The presets used to simplify ordering by eliminating the need
for price ids when submitting orders.
Also when the order contains a preset id, it is not possible
to configure VLANs in the order.

Important manual pages:
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Hardware_Server
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Item_Price
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/verifyOrder
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order_Hardware_Server

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer
import json

# Your SoftLayer API username and key.
API_USERNAME = 'set-me'

# Generate one at https://control.softlayer.com/account/users
API_KEY = 'set-me'

quantity = 1
location = 'DALLAS'
packageId = 200
presetId = 157

# Building a skeleton SoftLayer_Hardware_Server object to model the hostname and
# domain we want for our server. If you set quantity greater then 1 then you
# need to define one hostname/domain pair per server you wish to order.
hardware = [
    {
        'hostname': 'test',
        'domain': 'example.org'
    }
]

# Building a skeleton SoftLayer_Product_Item_Price objects. These objects contain
# much more than ids, but SoftLayer's ordering system only needs the price's id
# to know what you want to order.
# Every item in SoftLayer's product catalog is assigned an id. Use these ids
# to tell the SoftLayer API which options you want in your new server. Use
# the getActivePackages() method in the SoftLayer_Account API service to get
# a list of available item and price options per available package.
# Note: The presets already have some preconfigured items, such as
# the server or the disks you do not need to configure the prices for those
# items.
prices = [
    {'id': 44988},  # CentOS 7.x (64 bit)
    {'id': 1800},  # 0 GB Bandwidth
    {'id': 273},  # 100 Mbps Public & Private Network Uplinks
    {'id': 420},  # Unlimited SSL VPN Users & 1 PPTP VPN User per account
    {'id': 21},  # 1 IP Address
    {'id': 906}  # Reboot / KVM over IP
]

# Building a skeleton SoftLayer_Container_Product_Order_Hardware_Server object
# containing the order you wish to place.
orderTemplate = {
    'quantity': quantity,
    'location': location,
    'packageId': packageId,
    'prices': prices,
    'hardware': hardware,
    'presetId': presetId
}

# Creating a SoftLayer API client object
client = SoftLayer.create_client_from_env(username=API_USERNAME, api_key=API_KEY)

try:
    # verifyOrder() will check your order for errors. Replace this with a call
    # to placeOrder() when you're ready to order. Both calls return a receipt
    # object that you can use for your records.
    # Once your order is placed it'll go through SoftLayer's approval and
    # provisioning process. When it's done you'll have a new
    # SoftLayer_Hardware_Server object and server ready to use.
    receipt = client['Product_Order'].verifyOrder(orderTemplate)
    print(json.dumps(receipt, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to place a server order: \nfaultCode= %s, \nfaultString= %s"
          % (e.faultCode, e.faultString))
    exit(1)

```
