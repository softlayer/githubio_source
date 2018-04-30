---
title: "get_item_price_information.py"
description: "get_item_price_information.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Product_Package"
tags:
    - "package"
---


```
"""
Get item prices information

This script retrieves information of prices from a package. It retrieves the item description,
location conflicts, pricing location group and item conflicts

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Package/getRegions
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Package/getItemPrices
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Package/getItemPrices
http://sldn.softlayer.com/article/object-masks

@License: http://sldn.softlayer.com/article/License
@Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
# So we can talk to the SoftLayer API:
import SoftLayer
from prettytable import PrettyTable
# Your SoftLayer API username and key.
API_USERNAME = 'set me'
API_KEY = 'set me'
# Declare the image template id
packageId = 265
# Create a client instance
client = SoftLayer.Client(username=API_USERNAME, api_key=API_KEY)
# Declare an object mask to get location conflicts
objectMask = 'mask[pricingLocationGroup[locations],item[locationConflicts, conflicts]]'

try:
    locations = client['SoftLayer_Product_Package'].getRegions(id=packageId)
    items = client['SoftLayer_Product_Package'].getItems(id=packageId)
    print('*****  AVAILABLE LOCATIONS  *****')
    for location in locations:
        print('Id: %s,  Location: %s' % (location['location']['location']['id'], location['location']['location']['longName']))
    itemPrices = client['SoftLayer_Product_Package'].getItemPrices(id=packageId, mask=objectMask)
    x = PrettyTable(["Price Id", "Item Id", "Description", "Datacenter conflicts", "Pricing Location", 'Item conflicts'])
    x.align["Price Id"] = "l"  # Left align city names
    x.padding_width = 1
    for price in itemPrices:
        dcConflicts = ''
        pricingLocation = ''
        itemConflicts = ''
        # Get location conflicts
        if  len(price['item']['locationConflicts']) > 0:
            for locationConflicts in price['item']['locationConflicts']:
                for location in locations:
                    if locationConflicts['resourceTableId'] == location['location']['location']['id']:
                        dcConflicts = dcConflicts + ' ' + location['location']['location']['longName']
        else:
            dcConflicts = "None"
        # Get Pricing location
        if 'pricingLocationGroup' in price:
            for priceLocation in price['pricingLocationGroup']['locations']:
                pricingLocation = pricingLocation + ' ' + priceLocation['longName']
        else:
            pricingLocation = 'Standard price'
        # Get item conflicts
        if len(price['item']['conflicts']) > 0:
            for conflict in price['item']['conflicts']:
                itemConflicts = itemConflicts + ' ' + str(conflict['resourceTableId'])
        else:
            conflictItems = 'None'
        x.add_row([price['id'], price['item']['id'], price['item']['description'], dcConflicts, pricingLocation, itemConflicts])
    print(x)
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to get item prices faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))
    exit(1)

```
