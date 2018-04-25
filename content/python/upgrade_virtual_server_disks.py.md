---
title: "upgrade_virtual_server_disks.py"
description: "upgrade_virtual_server_disks.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
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
Upgrades a VSI

The script upgrades a VSI, it changes the size of a disk and add a new disk to the VSI
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

"""
The id of the virtual guest you wish upgrade
you can get the virtual guest ID by calling the SoftLayer_Account::getVirtualGuests method
for more reference see: http://sldn.softlayer.com/reference/services/SoftLayer_Account/getVirtualGuests
eg.
client = SoftLayer.Client(username=username,api_key=key)
accountService = client['SoftLayer_Account']
virtualServers = accountService.getVirtualGuests();
print (virtualServers)
"""
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
in this case we are adding two disk to our virtual server.
to get the list of prices and category codes available for the virtual server you can call the SoftLayer_Virtual_Guest::getUpgradeItemPrices method
for more reference see: http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/getUpgradeItemPrices
e.g.
client = SoftLayer.Client(username=username,api_key=key)
virtualGuestService = client['SoftLayer_Virtual_Guest']
virtualGuestID = 4949592 #the virtual guest ID of the machine which you want to upgrade
objectMask = "mask[item[attributes[attributeTypeKeyName]]]" # a mask to get some relational data from the result of SoftLayer_Virtual_Guest::getUpgradeItemPrices method
itemsToUpgrade = virtualGuestService.getUpgradeItemPrices(mask = objectMask, id = virtualGuestID );
print (itemsToUpgrade)
"""
prices = [
    {
        'id': 2277,
        'categories': [
            {
                'categoryCode': 'guest_disk1',
                'complexType': 'SoftLayer_Product_Item_Category'
            }
        ],
        'complexType': 'SoftLayer_Product_Item_Price'
    },

    {
        'id': 2270,
        'categories': [
            {
                'categoryCode': 'guest_disk2',
                'complexType': 'SoftLayer_Product_Item_Category'
            }
        ],
        'complexType': 'SoftLayer_Product_Item_Price'
    }
]

"""
Build a skeleton SoftLayer_Container_Product_Order_Property objects
in this case the upgrade will be immediately.
"""
properties = [
    # modeling the note for the upgrade
    {
        'name': 'NOTE_GENERAL',
        'value': 'adding disks'
    },

    # modeling the date for the upgrade
    {
        'name': 'MAINTENANCE_WINDOW',
        'value': '2014-08-25T9:50:00-05:00'
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
productOrderService = client['SoftLayer_Product_Order']

try:
    """
    Upgrading the virtual guest
    you can use verifyOrder method to test that your upgrade is fine
    when you are ready you can call the placeOrder method.
    for more reference see:
    http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order
    http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/verifyOrder
    http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder
    """
    result = productOrderService.verifyOrder(upgradeData)
    print(result)
except SoftLayer.SoftLayerAPIError as e:
    """
    If there was an error returned from the SoftLayer API then bomb out with the
    error message.
    """
    print("Unable to upgrade VSI faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))

```
