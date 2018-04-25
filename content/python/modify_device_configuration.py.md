---
title: "modify_device_configuration.py"
description: "modify_device_configuration.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Container_Product_Order_Hardware_Server_Upgrade"
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Container_Product_Order_Property"
    - "SoftLayer_Hardware_Server"
    - "SoftLayer_Product_Order"
tags:
    - "baremetalservers"
---


```
"""
Upgrades a server.

Important manual pages
http://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server/findByIpAddress
http://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server/getUpgradeItemPrices
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/verifyOrder
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Item_Price
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order_Property
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order_Hardware_Server_Upgrade

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer.API
import json


def getServer(serverIp, hardwareService):
    """Get the server.
         :param string serverIp: The Ip address of the server.
         :param SoftLayer_Hardware_Server hardwareService: the SoftLayer_Hardware_Server service.
         :returns: A SoftLayer_Hardware_Server object.
    """
    try:
        objectMask = "mask[id]"
        server = hardwareService.findByIpAddress(serverIp, mask=objectMask)
        if not server:
            print("There is no a server with the IP address: " + serverIp)
            exit(1)
    except SoftLayer.SoftLayerAPIError as e:
        print("Unable to retrieve the server:" % (e.faultCode, e.faultString))
        exit(1)
    return server


def getUpgradeItems(server, hardwareService):
    """Get the prices of the items to upgrade in a server.
         :param SoftLayer_Hardware_Server server: The server to get the upgrade item prices.
         :param SoftLayer_Hardware_Server hardwareService: the SoftLayer_Hardware_Server service.
         :returns: A array of SoftLayer_Product_Item_Price object.
    """
    try:
        upgradeItems = hardwareService.getUpgradeItemPrices(id=server['id'])
    except SoftLayer.SoftLayerAPIError as e:
        print("Unable to retrieve the upgrade items:" % (e.faultCode, e.faultString))
        exit(1)
    return upgradeItems

# Your SoftLayer API username and key.
API_USERNAME = 'set-me'

# Generate one at https://control.softlayer.com/account/users
API_KEY = 'set-me'

serverIp = "159.8.52.186"

# Specify the items to upgrade and the values.
# It uses the same names and values as the displayed
# in Softlayer's Portal.
modify = {
    "FIRST HARD DRIVE": "2.00 TB SATA",
    "SECOND HARD DRIVE": "500 GB SATA"
}

# The date for the upgrade of the server.
dateForUpgrade = "INMEDIATELY"

client = SoftLayer.create_client_from_env(username=API_USERNAME, api_key=API_KEY)
hardwareService = client['SoftLayer_Hardware_Server']
productOrderService = client['SoftLayer_Product_Order']

server = getServer(serverIp, hardwareService)
pricesUpgrade = getUpgradeItems(server, hardwareService)

# Getting the item prices for the upgrade.
prices = []
for item in modify.keys():
    for price in pricesUpgrade:
        added = False
        for category in price['categories']:
            if category['name'].strip().upper() == item.strip().upper() and \
               price['item']['description'].strip().upper() == modify[item].strip().upper():
                prices.append(price)
                added = True
                break
        if added:
            break
    if not added:
        print("There is no price for the item: " + item + "- " + modify[item])


# Build a skeleton SoftLayer_Container_Product_Order_Property objects
properties = [
    {
        'name': 'MAINTENANCE_WINDOW',
        'value': dateForUpgrade
    },
    {
        'name': 'MAINTENANCE_WINDOW_ID',
        'value': 483
    }
]

# Build a skeleton SoftLayer_Container_Product_Order_Hardware_Server_Upgrade object
# containing the upgrade you wish to place
upgradeData = {
    'hardware': [server],
    'prices': prices,
    'properties': properties,
    'complexType': 'SoftLayer_Container_Product_Order_Hardware_Server_Upgrade'
}

try:
    # When you are ready to upgrade the server
    # change veryOrder() method by placeOrder method.
    result = productOrderService.verifyOrder(upgradeData)
    print(json.dumps(result, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to upgrade bare metal server: \nfaultCode= %s, \nfaultString= %s" % (e.faultCode, e.faultString))

```
