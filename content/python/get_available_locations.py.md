---
title: "get_available_locations.py"
description: "get_available_locations.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Product_Package"
    - "SoftLayer_Product_Item"
tags:
    - "package"
---


```
"""
Get available locations.

This script will retrieve a collection of valid locations for a given package and the server.
It displays the same locations as Control Portal does.
E.g: Portal Link: https://manage.softlayer.com/Sales/configureOrder/265/49565/
package = 265
server = 49565
Important manual pages:

http://sldn.softlayer.com/reference/services/SoftLayer_Product_Package/getRegions
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Item_Price/getItem
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Item
@License: http://sldn.softlayer.com/article/License
@Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

# So we can talk to the SoftLayer API:
import SoftLayer

# Your SoftLayer API username and key.
API_USERNAME = 'set me'
API_KEY = 'set me'
# Declare the package id
package = 200
# Declare the server id
server = 37318
# Create a client instance
client = SoftLayer.Client(username=API_USERNAME, api_key=API_KEY)
# Declare an object mask to get location conflicts for the server
priceMask = 'mask[locationConflicts]'
try:
    flag = False
    locations = client['SoftLayer_Product_Package'].getRegions(id=package)
    locationConflicts = client['SoftLayer_Product_Item_Price'].getItem(id=server, mask=priceMask)
    print('*****   AVAILABLE LOCATIONS   *****')
    for location in locations:
        for locationConflict in locationConflicts['locationConflicts']:
            if location['location']['location']['id'] == locationConflict['resourceTableId']:
                flag = False
        if flag:
            print('Id: %s, Location Name: %s' % (location['location']['location']['id'], location['location']['location']['longName']))
        flag = True
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to get available locations faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))
    exit(1)

```
