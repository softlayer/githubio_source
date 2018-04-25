---
title: "create_bare_metal.py"
description: "create_bare_metal.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Container_Product_Order"
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Hardware_Server"
    - "SoftLayer_Product_Package"
    - "SoftLayer_Container_Product_Order_Hardware_Server"
    - "SoftLayer_Product_Order"
tags:
    - "baremetalservers"
---


```
"""
Order a new server.

Build a SoftLayer_Container_Product_Order object for a new server order
and pass it to the SoftLayer_Product_Order API service to order it.
In this care we'll order a Single Intel Xeon E5-2620 with 8G RAM, 100mbit NICs,
500GB bandwidth, a 500G SATA drive, no Operating system, and default server order options.
See below for more details.

Important manual pages:
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Hardware_Server
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Item_Price
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/verifyOrder
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder
https://sldn.softlayer.com/reference/services/SoftLayer_Account/getActivePackages

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer

# For nice debug output:
from pprint import pprint as pp

# Your SoftLayer API username and key.
API_USERNAME = 'set-me'

# Generate one at https://control.softlayer.com/account/users
API_KEY = 'set-me'

# The number of servers you wish to order in this configuration.
quantity = 1

"""
Where you'd like your new server provisioned.

This can either set the id of the datacenter you wish your new server to be
provisioned in or the string.

Location id 3     = Dallas
Location id 18171 = Seattle
Location id 37473 = Washington, D.C.
"""
location = 'AMSTERDAM'

"""
The id of the SoftLayer_Product_Package you wish to order.
In this case the Intel Xeon 3460's package id is 145.
"""
packageId = 259

"""
Build a skeleton SoftLayer_Hardware_Server object to model the hostname and
domain we want for our server. If you set quantity greater then 1 then you
need to define one hostname/domain pair per server you wish to order.
"""
hardware = [
    {
        'hostname': 'test',  # The hostname of the server you wish to order.
        'domain': 'example.org'  # The domain name of the server you wish to order.
    }
]

"""
Build a skeleton of SoftLayer_Product_Item_Price objects. These objects contain
much more than ids, but SoftLayer's ordering system only needs the price's id
to know what you want to order.

Every item in SoftLayer's product catalog is assigned an id. Use these ids
to tell the SoftLayer API which options you want in your new server. Use
the getActivePackages() method in the SoftLayer_Account API service to get
a list of available item and price options per available package.
"""
prices = [
    {'id': 179861},  # server: Single  Intel  Xeon  E5-2620 (6 Cores, 2.00 GHz)
    {'id': 76165},  # ram: 8 GB RAM
    {'id': 37120},  # os: No Operating System
    {'id': 876},  # disk_controller: Non-RAID
    {'id': 69535},  # disk0: 500 GB SATA
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

"""
Build a skeleton SoftLayer_Container_Product_Order_Hardware_Server object
containing the order you wish to place.
"""
orderTemplate = {
    'quantity': quantity,
    'location': location,
    'packageId': packageId,
    'prices': prices,
    'hardware': hardware
}

# Create a SoftLayer API client object
client = SoftLayer.create_client_from_env(username=API_USERNAME, api_key=API_KEY)

try:
    """
    verifyOrder() will check your order for errors. Replace this with a call
    to placeOrder() when you're ready to order. Both calls return a receipt
    object that you can use for your records.

    Once your order is placed it'll go through SoftLayer's approval and
    provisioning process. When it's done you'll have a new
    SoftLayer_Hardware_Server object and server ready to use.
    """
    receipt = client['Product_Order'].verifyOrder(orderTemplate)
    pp(receipt)
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to place a server order  \nfaultCode= %s, \nfaultString= %s"
          % (e.faultCode, e.faultString))
    exit(1)

```
