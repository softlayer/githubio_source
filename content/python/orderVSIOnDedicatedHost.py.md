---
title: "orderVSIOnDedicatedHost.py"
description: "orderVSIOnDedicatedHost.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Container_Product_Order_Virtual_Guest"
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Container_Product_Order"
    - "SoftLayer_Product_Order"
    - "SoftLayer_Product_Item_Price"
tags:
    - "dedicatedhost"
---


```
"""
Order a new VSI in a dedicated host.

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

USERNAME = 'setme'
API_KEY = 'setme'

orderData = {
    "complexType": "SoftLayer_Container_Product_Order_Virtual_Guest",
    "hostId": 9301, # The dedicated host where this virtual guest is going to be deployed in
    "packageId": 46,
    "prices": [
        {"id": 200317},
        {"id": 200353},
        {"id": 45466},
        {"id": 200385},
        {"id": 50367},
        {"id": 273},
        {"id": 55},
        {"id": 58},
        {"id": 420},
        {"id": 418},
        {"id": 21},
        {"id": 57},
        {"id": 905}
    ],
    "quantity": 1,
    "virtualGuests": [
        {
            "domain": "softlayer.com",
            "hostname": "rcabtestdein2",
            "primaryBackendNetworkComponent": {
                "networkVlan": {
                    "id": 1404269,
                    "primarySubnet": 1314283
                }
            },
            "primaryNetworkComponent": {
                "networkVlan": {
                    "id": 1404267,
                    "primarySubnet": {
                        "id": 1319803
                    }
                }
            },
            "userData": [
                {"value": "metadata"}
            ]
        }
    ],
    "provisionScripts": [
        "http://examples.provisioning.org"
    ],
    "sshKeys": [
        {
            "sshKeyIds": [94206]
        }
    ]
}


client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)

"""
verifyOrder() will check your order for errors. Replace this with a call to
placeOrder() when you're ready to order. Both calls return a receipt object
that you can use for your records.

Once your order is placed it'll go through SoftLayer's provisioning process.
When it's done you'll have a new virtual guest ready
to use.
"""
try:
    result = client['Product_Order'].verifyOrder(orderData)
    print (result)
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to place the order. faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))

```
