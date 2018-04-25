---
title: "upgrade_bare_metal_server.py"
description: "upgrade_bare_metal_server.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Container_Product_Order_Property"
    - "SoftLayer_Container_Product_Order_Hardware_Server_Upgrade"
    - "SoftLayer_Hardware"
    - "SoftLayer_Product_Order"
tags:
    - "upgrade"
---


```
"""
Upgrades a Bare Metal Server

The script upgrades a Bare Metal server, it changes port speed to 1GB
for more information see below:

Important manual pages
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Item_Price
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order_Property
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order_Hardware_Server_Upgrade
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/verifyOrder
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer

USERNAME = 'set me'
API_KEY = 'set me'


# The id of the hardware you wish upgrade
hardwareServerId = 166391


# Build a skeleton SoftLayer_Hardware object to model the id
hardwareServer = [
    {
        'id': hardwareServerId
    }
]

"""
Build a skeleton SoftLayer_Product_Item_Price objects
Every item in SoftLayer's product catalog is assigned an id. Use these ids
to tell the SoftLayer API which options you want in your new server
"""
prices = [
    {
        'id': 2314,  # The price of the new port speed
        'categories': [
            {
                'categoryCode': 'port_speed'
            }
        ]
    }
]

# Build a skeleton SoftLayer_Container_Product_Order_Property objects
properties = [
    # modeling the note for the upgrade
    {
        'name': 'NOTE_GENERAL',
        'value': 'upgrade de port speeds to 1 Gbps'
    },

    # modeling the date for the upgrade
    {
        'name': 'MAINTENANCE_WINDOW',
        'value': '2014-10-30T03:00:00-05:00'
    },

    {
        'name': 'MAINTENANCE_WINDOW_ID',
        'value': 483
    }

]

"""
Build a skeleton SoftLayer_Container_Product_Order_Hardware_Server_Upgrade object
containing the upgrade you wish to place.
"""
upgradeData = {
    'hardware': hardwareServer,
    'prices': prices,
    'properties': properties,
    'complexType': 'SoftLayer_Container_Product_Order_Hardware_Server_Upgrade'
}

# Declare a new API service object
client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)


try:
    # upgrading the virtual guest
    result = client['SoftLayer_Product_Order'].placeOrder(upgradeData)
    print(result)
except SoftLayer.SoftLayerAPIError as e:
    """
    If there was an error returned from the SoftLayer API then bomb out with the
    error message.
    """

    print("Unable to upgrade bare metal server faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))

```
