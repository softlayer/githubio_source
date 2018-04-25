---
title: "create_vsi_no_monitoring.py"
description: "create_vsi_no_monitoring.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Container_Product_Order_Virtual_Guest"
    - "SoftLayer_Account"
    - "SoftLayer_Container_Product_Order"
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Hardware_Server"
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Product_Package"
    - "SoftLayer_Product_Order"
tags:
    - "virtualserver"
---


```
"""
Order a new VSI without advanced monitoring.

The script makes a order for a VSI, it uses the SoftLayer_Product_Order::placeOrder method
for more information please see below:

Important manual pages:
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_Guest
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Item_Price
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/verifyOrder
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
import SoftLayer

# For nice debug output:
from pprint import pprint as pp

# Your SoftLayer API username and key.
API_USERNAME = 'set me'

# Generate one at https://control.softlayer.com/account/users
API_KEY = 'set me'

"""
Build a skeleton SoftLayer_Container_Product_Order_Virtual_Guest object
containing the order you wish to place.
"""
orderData = {
    # The id of the SoftLayer_Product_Package you wish to order.
    "packageId": 46,
    # Where you'd like your new server provisioned.
    # This can either be the id of the data center you wish your new server to be
    # provisioned in or the string 'FIRST_AVAILABLE' if you have no preference
    # where your server is provisioned.
    # Location id 3     = Dallas
    # Location id 18171 = Seattle
    # Location id 37473 = Washington, D.C.
    "location": "AMSTERDAM",
    # Build a skeleton SoftLayer_Product_Item_Price objects. These objects contain
    # much more than Ids, but SoftLayer's ordering system only needs the price's id
    # to know what you want to order.

    # Every item in SoftLayer's product catalog is assigned an id. Use these ids
    # to tell the SoftLayer API which options you want in your new server. Use
    # the getActivePackages() method in the SoftLayer_Account API service to get
    # a list of available item and price options per available package.
    "prices":
        [
            {"id": 1962}, # 1 x 2.0 GHz Cores (Dedicated)
            {"id": 1644}, # 1 GB
            {"id": 22267}, # Debian GNU\/Linux 7.x Wheezy\/Stable - Minimal Install (64 bit)
            {"id": 2202}, # 25 GB (SAN)
            {"id": 2255}, # 10 GB (SAN) - GUEST_DISK_10_GB_SAN
            {"id": 905}, # Reboot \/ Remote Console
            {"id": 272}, # 10 Mbps Public & Private Network Uplinks
            {"id": 1800}, # 0 GB Bandwidth
            {"id": 21}, # 1 IP Address
            {"id": 55}, # Host Ping
            {"id": 57}, # Email and Ticket
            {"id": 58}, # Automated Notification
            {"id": 420}, # Unlimited SSL VPN Users & 1 PPTP VPN User per account
            {"id": 418} # Nessus Vulnerability Assessment & Reporting
        ],
    # The number of servers you wish to order in this configuration.
    "quantity": 1,
    # Build a skeleton SoftLayer_Virtual_Guest object to model the hostname,
    # domain and the VLANs we want for our server. If you set quantity greater
    # then 1 then you need to define one hostname/domain pair per server you wish to order.
    # note: if you want order a Bare Metal you need to model a SoftLayer_Hardware_Server
    "virtualGuests":
        [
            {
                "domain": "softlayer.ibm.com",
                "hostname": "VM1",
            }
        ]
    }

# Declare a new API service object
client = SoftLayer.create_client_from_env(username=API_USERNAME, api_key=API_KEY)

"""
verifyOrder() will check your order for errors. Replace this with a call to
placeOrder() when you're ready to order. Both calls return a receipt object
that you can use for your records.

Once your order is placed it'll go through SoftLayer's provisioning process.
When it's done you'll have a new SoftLayer_Virtual_Guest object and CCI ready
to use.
"""
try:
    result = client['Product_Order'].verifyOrder(orderData, False)
    pp(result)
except SoftLayer.SoftLayerAPIError as e:
    """
    If there was an error returned from the SoftLayer API then bomb out with the
    error message.
    """
    print("Unable make the order faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))

```
