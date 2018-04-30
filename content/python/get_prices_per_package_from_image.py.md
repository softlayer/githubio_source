---
title: "get_prices_per_package_from_image.py"
description: "get_prices_per_package_from_image.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Product_Package"
    - "SoftLayer_Virtual_Guest_Block_Device_Template_Group"
tags:
    - "package"
---


```
"""
This script retrieves item prices per packages from an image template

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Package/getAvailablePackagesForImageTemplate
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Package/getItemsFromImageTemplate
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_Guest_Block_Device_Template_Group

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
imageTemplateId = 33566
# Create a client instance
client = SoftLayer.Client(username=API_USERNAME, api_key=API_KEY)
# Build a SoftLayer_VIrtual_Guest_Block_Device_Template_Group object
imageTemplate = {
                "id": imageTemplateId
                }
# Declare an object mask to get prices for items
priceMask = 'mask[pricingLocationGroup[locations]]'
try:
    # Get available packages for the image template
    packages = client['SoftLayer_Product_Package'].getAvailablePackagesForImageTemplate(imageTemplate)
    for package in packages:
        # Build table
        x = PrettyTable(["Price Id", "Item Id", "Description", "Datacenters"])
        x.align["Price Id"] = "l"  # Left align city names
        x.padding_width = 1
        print('***** Package: %s *****' % package['id'])
        # Get Item Prices, in order to verify the active prices
        itemPrices = client['SoftLayer_Product_Package'].getItemPrices(id=package['id'], mask=priceMask)
        # Get Items from the image template
        items = client['SoftLayer_Product_Package'].getItemsFromImageTemplate(imageTemplate, id=package['id'])
        # We define a item verification, in order to avoid duplicate data in the loop
        itemVerication = 0
        for item in items:
            if item['id'] != itemVerication:
                for itemPrice in itemPrices:
                    if itemPrice['item']['id'] == item['id']:
                        locationDC = ''
                        pack = ''
                        if 'pricingLocationGroup' in itemPrice:
                            for locations in itemPrice['pricingLocationGroup']['locations']:
                                locationDC = locationDC + ' ' + locations['longName']
                        else:
                            locationDC = 'Standard price'
                        x.add_row([itemPrice['id'], itemPrice['item']['id'], itemPrice['item']['description'], locationDC])
                itemVerication = item['id']
        print(x)
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to get prices for packages from an image template faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))
    exit(1)

```
