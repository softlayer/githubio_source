---
title: "upgrade_virtual_server.py"
description: "upgrade_virtual_server.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Product_Item_Category"
    - "SoftLayer_Container_Product_Order_Virtual_Guest_Upgrade"
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Container_Product_Order_Property"
    - "SoftLayer_Product_Order"
tags:
    - "upgrade"
---


```
"""
Upgrades the ram of a VSI

The script upgrades a VSI, it upgrades the ram from 1GB to 2GB
for more information see below:

Important manual pages
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Item_Category
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_Guest
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_Guest
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order_Virtual_Guest_Upgrade
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/verifyOrder
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer

USERNAME = 'set me'
API_KEY = 'set me'

# The id of the virtual guest you wish upgrade
virtualGuestId = 4949592


# Build a skeleton SoftLayer_Virtual_Guest object to model the id
virtualGuest = [
    {
        'id': virtualGuestId
    }
]

"""
Build a skeleton SoftLayer_Product_Item_Price objects
Every item in SoftLayer's product catalog is assigned an id. Use these ids
to tell the SoftLayer API which options you want in your new server
"""
prices = [
    {
        'id': 1645,  # The price of ram 2GB
        'categories': [
            {
                'categoryCode': 'ram'
            }
        ]
    }
]

# Build a skeleton SoftLayer_Container_Product_Order_Property objects
properties = [
    # Modeling the note for the upgrade
    {
        'name': 'NOTE_GENERAL',
        'value': 'upgrading ram to 2 GB'
    },

    # Modeling the date for the upgrade
    {
        'name': 'MAINTENANCE_WINDOW',
        'value': '2014-06-21T04:00:00+12:00'
    },

    {
        'name': 'MAINTENANCE_WINDOW_ID',
        'value': 486
    }

]

"""
Build a skeleton SoftLayer_Container_Product_Order_Virtual_Guest_Upgrade object
containing the upgrade you wish to place.
"""
upgradeData = {
    'virtualGuests': virtualGuest,
    'prices': prices,
    'properties': properties,
    'complexType': 'SoftLayer_Container_Product_Order_Virtual_Guest_Upgrade'
}

# Declare a new API service object
client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)

try:
    # Upgrading the virtual guest
    result = client['SoftLayer_Product_Order'].placeOrder(upgradeData)
    print(result)
except SoftLayer.SoftLayerAPIError as e:
    """
    If there was an error returned from the SoftLayer API then bomb out with the
    error message.
    """
    print("Unable to upgrade VSI faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))

```
