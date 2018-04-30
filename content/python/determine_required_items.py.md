---
title: "determine_required_items.py"
description: "determine_required_items.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Product_Package"
tags:
    - "package"
---


```
"""
Determine Required items
Each Package is aware of a list of ItemCategories that make sense for that Package.
This list is called the Packages "Configuration". Within the configuration,
the Package may identify certain categories that are required, meaning you must include
an ItemPrice from that category in any order you make against that Package

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Package/getConfiguration
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Package/getItemPrices
http://sldn.softlayer.com/article/Python
@License: http://sldn.softlayer.com/article/License
@Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
import SoftLayer

API_USERNAME = 'set-me'
API_KEY = 'set-me'
package = 46

client = SoftLayer.Client(username=API_USERNAME, api_key=API_KEY)
"""
Only retrieve the boolean to determine if this category
is required and the category name and ID
"""
categoryObjectMask = "mask[isRequired, itemCategory[id, name]]"

# Retrieve a list of category configurations associated with our chosen package
configurations = client['Product_Package'].getConfiguration(mask=categoryObjectMask, id=package)
"""
For each price we only want the id, the ID of the category(ies) it is a member of,
and the item description
"""
pricesObjectMask = "mask[id;item.description;categories.id]"

# Get all itemPrices for this package
prices = client['SoftLayer_Product_Package'].getItemPrices(mask=pricesObjectMask, id=package)

# Text format for our prettified output
headerFormat = '%s - %s:'
priceFormat = '    %s -- %s'

for configuration in configurations:
    """
    We are only concerned with required categories...
    skip it if we do not need it!
    """
    if not configuration['isRequired']:
        continue
    print(headerFormat % (configuration['itemCategory']['name'],
                          configuration['itemCategory']['id']))
    for price in prices:
        if 'categories' not in price:
            continue
        l = list(filter(lambda x: x.get('id') == configuration['itemCategory']['id'], price['categories']))
        if len(l):
            print(priceFormat % (price['id'], price['item']['description']))

```
