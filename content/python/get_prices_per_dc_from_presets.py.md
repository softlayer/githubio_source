---
title: "get_prices_per_dc_from_presets.py"
description: "get_prices_per_dc_from_presets.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Product_Package"
tags:
    - "package"
---


```
"""
Get active presets and their prices per location

This script retrieves the active presets with their prices for the items per datacenter.
Also it displays the information for hourly recurring fee and recurring fee.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Package/getActivePresets
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Package/getItemPrices
http://sldn.softlayer.com/search/site/object%20mask
http://sldn.softlayer.com/article/Object-Filters

@License: http://sldn.softlayer.com/article/License
@Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
# So we can talk to the SoftLayer API:
import SoftLayer
from prettytable import PrettyTable

# Your SoftLayer API username and key.
API_USERNAME = 'set me'
API_KEY = 'set me'
# Declare the package id
packageId = 200
# Create a client instance
client = SoftLayer.Client(username=API_USERNAME, api_key=API_KEY)
# Declare an object mask to get prices and items information
objectMask = 'mask[prices[item]]'
# Declare an object mask to get pricingLocationGroup
objectMaskPrice = 'mask[pricingLocationGroup[locations]]'
try:
    # Get active presets
    activePresets = client['SoftLayer_Product_Package'].getActivePresets(id=packageId, mask=objectMask)
    for activePreset in activePresets:
        print('**************   PRESET ID: %s   **************' % activePreset['id'])
        # Configuring table's columns
        x = PrettyTable(['Locations', 'Price Id', 'Item Id', 'Item Description', 'hourlyRecurringFee', 'recurringFee'])
        x.padding_width = 1
        print('Id: %s, Description: %s, isActive: %s' % (activePreset['id'], activePreset['description'], activePreset['isActive']))
        print('        KeyName: %s, Name: %s' % (activePreset['keyName'], activePreset['name']))
        for prices in activePreset['prices']:
            print('                 Price Id: %s, Item Id: %s Item Description: %s' % (prices['id'], prices['item']['id'], prices['item']['description']))
            objectFilterItem = {'itemPrices': {'item': {'id': {'operation': prices['item']['id']}}}}
            prices = client['SoftLayer_Product_Package'].getItemPrices(id=200, filter=objectFilterItem, mask=objectMaskPrice)
            for price in prices:
                locationDisplay = ''
                recurringFee = 0
                # Verifying if the price has pricingLocationGroup
                if 'pricingLocationGroup' in price:
                    for location in price['pricingLocationGroup']['locations']:
                        locationDisplay = locationDisplay + ' ' + location['longName']
                else:
                    locationDisplay = 'STANDARD PRICE'
                # Verifying if the price has Recurring Fee
                if 'recurringFee' in price:
                    recurringFee = price['recurringFee']
                else:
                    recurringFee = 'null'
                x.add_row([locationDisplay, price['id'], price['item']['id'], price['item']['description'], price['hourlyRecurringFee'], recurringFee])
        print(x)
except SoftLayer.SoftLayerAPIError as e:
    print('Unable to get active presets faultCode=%s, faultString=%s' % (e.faultCode, e.faultString))
    exit(1)

```
