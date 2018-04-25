---
title: "get_active_presets_prices.py"
description: "get_active_presets_prices.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Product_Package"
    - "SoftLayer_Product_Package_Preset"
tags:
    - "package"
---


```
"""
Get active presets prices

This script retrieves the available preset configurations for this package, also
it provides information about the prices and items from them.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Package/getActivePresets
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Package_Preset

@License: http://sldn.softlayer.com/article/License
@Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

# So we can talk to the SoftLayer API:
import SoftLayer

# Your SoftLayer API username and key.
API_USERNAME = 'set me'
API_KEY = 'set me'
# Declare the package id
packageId = 200
# Create a client instance
client = SoftLayer.Client(username=API_USERNAME, api_key=API_KEY)
# Declare an object mask to get prices and items information
objectMask = 'mask[prices[item]]'
try:
    activePresets = client['SoftLayer_Product_Package'].getActivePresets(id=packageId, mask=objectMask)
    for activePreset in activePresets:
        print('Id: %s, Description: %s, isActive: %s' % (activePreset['id'], activePreset['description'], activePreset['isActive']))
        print('        KeyName: %s, Name: %s' % (activePreset['keyName'], activePreset['name']))
        for prices in activePreset['prices']:
            print('                 Price Id: %s, Item Id: %s Item Description: %s' % (prices['id'], prices['item']['id'], prices['item']['description']))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to get active presets faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))
    exit(1)

```
