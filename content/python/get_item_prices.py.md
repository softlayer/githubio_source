---
title: "get_item_prices.py"
description: "get_item_prices.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Product_Package"
tags:
    - "package"
---


```
"""
Get item prices

This script will display the  general information relating
to a single SoftLayer product item price
Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Package/getItemPrices
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Item_Price
@License: http://sldn.softlayer.com/article/License
@Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
# So we can talk to the SoftLayer API:
import SoftLayer

# Your SoftLayer API username and key.
API_USERNAME = 'set-me'
API_KEY = 'set-me'

# Set the ID of the package to retrieve the information
package = 46
# Create a client instance
client = SoftLayer.Client(username=API_USERNAME, api_key=API_KEY)
# Text format for our prettified output
headerFormat = '%s - %s:'
itemFormat = '    %s:'
categoryFormat = '         %s -- %s'

# Set the object mask to retrieve categories
categoryObjectMask = 'mask[categories]'
# Get all item prices for this package
prices = client['SoftLayer_Product_Package'].getItemPrices(mask=categoryObjectMask, id=package)
for price in prices:
    print(headerFormat % ('Product item price', price['id']))
    if 'hourlyRecurringFee' in price:
        print('    %s - %s' % ('Hourly price(hourlyRecurringFee)', price['hourlyRecurringFee']))
    print(itemFormat % 'Item')
    print(categoryFormat % (price['item']['id'], price['item']['description']))
    categories = []
    if 'categories' in price:
        categories = price['categories']
        print(itemFormat % 'Categories')
        for category in categories:
            print(categoryFormat % (category['id'], category['name']))

```
