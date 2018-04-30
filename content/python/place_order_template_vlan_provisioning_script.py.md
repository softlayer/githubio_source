---
title: "place_order_template_vlan_provisioning_script.py"
description: "place_order_template_vlan_provisioning_script.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Container_Product_Order"
    - "SoftLayer_Product_Order"
    - "SoftLayer_Product_Item_Price"
tags:
    - "virtualserver"
---


```
"""
Order a new VSI with post script and VLAN.

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
"""

"""
# Your SoftLayer API username and key.
API_USERNAME = 'set me'

# Generate one at https://control.softlayer.com/account/users
API_KEY = 'set me'

orderData = {
    "imageTemplateId": "1656107",
    "packageId": 46,
    "location": "AMSTERDAM",
    "prices": [
        {"id": 1962},  # 1 x 2.0 GHz Cores (Dedicated)
        {"id": 1644},  # 1 GB
        {"id": 22267},  # Debian GNU\/Linux 7.x Wheezy\/Stable - Minimal Install (64 bit)
        {"id": 2202},  # 25 GB (SAN)
        {"id": 2255},  # 10 GB (SAN) - GUEST_DISK_10_GB_SAN
        {"id": 905},  # Reboot \/ Remote Console
        {"id": 272},  # 10 Mbps Public & Private Network Uplinks
        {"id": 1800},  # 0 GB Bandwidth
        {"id": 21},  # 1 IP Address
        {"id": 55},  # Host Ping
        {"id": 57},  # Email and Ticket
        {"id": 58},  # Automated Notification
        {"id": 420},  # Unlimited SSL VPN Users & 1 PPTP VPN User per account
        {"id": 418}  # Nessus Vulnerability Assessment & Reporting
               ],
    "quantity": 1,
    "hardware": [
                          {
                            "domain": "softlayer.ibm.com",
                            "hostname": "sptest1",
                            "primaryBackendNetworkComponent": {
                                                                 "networkVlanId": 1084325
                                                                },
                            "primaryNetworkComponent": {
                                                          "networkVlanId": 361652
                                                         }
                          }
                      ],
    "provisionScripts": [
                          "http://examples.provisioning.org"
                         ]
}


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
    result = client['Product_Order'].verifyOrder(orderData)
    pp (result)
except SoftLayer.SoftLayerAPIError as e:
    """
    If there was an error returned from the SoftLayer API then bomb out with the
    error message.
    """
    print("Unable to create the order. "
          % (e.faultCode, e.faultString))

```
