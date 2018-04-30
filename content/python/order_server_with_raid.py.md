---
title: "order_server_with_raid.py"
description: "order_server_with_raid.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Container_Product_Order"
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Product_Order"
    - "SoftLayer_Container_Product_Order_Storage_Group"
    - "SoftLayer_Container_Product_Order_Hardware_Server"
    - "SoftLayer_Hardware_Server"
tags:
    - "baremetalservers"
---


```
"""
Order a new server with RAID configuration.

Important manual pages:
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Hardware_Server
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Item_Price
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/verifyOrder
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder

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
location = 'AMSTERDAM'
packageId = 259
lvmFlag = True
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
prices = [
    {'id': 179861},  # server: Single  Intel  Xeon  E5-2620 (6 Cores, 2.00 GHz)
    {'id': 76165},  # ram: 8 GB RAM
    {'id': 44988},  # os: CentOS 7.x (64 bit)
    {'id': 74995},  # disk_controller: RAID
    {'id': 64769},  # disk0: 2.00 TB SATA
    {'id': 69535},  # disk1: 500 GB SATA
    {'id': 69535},  # disk2: 500 GB SATA
    {'id': 50357},  # bandwidth: 500 GB Bandwidth
    {'id': 273},  # port_speed: 100 Mbps Public & Private Network Uplinks
    {'id': 55},  # monitoring: Host Ping
    {'id': 58},  # response: Automated Notification
    {'id': 420},  # vpn_management: Unlimited SSL VPN Users & 1 PPTP VPN User per account
    {'id': 418},  # vulnerability_scanner: Nessus Vulnerability Assessment & Reporting
    {'id': 21},  # pri_ip_addresses: 1 IP Address
    {'id': 57},  # notification: Email and Ticket
    {'id': 906}  # remote_management: Reboot / KVM over IP
]

# Building a skeleton SoftLayer_Container_Product_Order_Storage_Group object
# Storage groups will only be used if the 'RAID' disk controller price is selected.
# Any other disk controller types will ignore the storage groups set here.
# The first storage group in this array will be considered the primary storage group,
# which is used for the OS. Any other storage groups will act as data storage.
storageGroups = [
    {
         "arraySize": 1000,
         "arrayTypeId": 3,  # RAID_5
         "hardDrives": [
            0,
            1,
            2
         ],
         "partitionTemplateId": 6
     },
    {
         "arraySize": 500,
         "arrayTypeId": 9,
         "hardDrives": [
             0
         ],
         # The custom partitions only work on other storage groups
         # different from the primary one
         "partitions": [
             {
                 "isGrow": False,
                 "name": "/test",
                 "size": 100
             },
             {
                 "isGrow": True,
                 "name": "/test2",
                 "size": 200
             }
         ]
     },
]

# Building a skeleton SoftLayer_Container_Product_Order_Hardware_Server object
# containing the order you wish to place.
orderTemplate = {
    'quantity': quantity,
    'location': location,
    'packageId': packageId,
    'prices': prices,
    'hardware': hardware,
    'storageGroups': storageGroups,
    'lvmFlag': lvmFlag
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
