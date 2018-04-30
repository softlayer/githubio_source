---
title: "filtersRuby.rb"
description: "filtersRuby.rb"
date: "2018-04-25"
classes: 
    - "SoftLayer_Product_Package"
tags:
    - "filters"
---


```
require 'softlayer_api'
require 'pp'

# Your SoftLayer API username and key.
# Generate an API key at the SoftLayer Customer Portal:
# https://manage.softlayer.com/Administrative/apiKeychain
username = ''
key = 'apikey_goes_here'

# The package ID you wish to see the prices list
packageId = 0
# The categoryID you which to filter the returned list by SoftLayer_Product_Package::getItemPrices method
categoryIDtofilter = 15

# Declare the API client
client = SoftLayer::Client.new( :username => username,:api_key => key)
productPackageService = client['SoftLayer_Product_Package']

# Declaring the object mask to get the item id, description and categoryId
objectMask = "mask[id,item.description,categories.id]"
# Declaring the object Filter to get only the categories with the id = categoryIDtofilter
objectFilter = {"itemPrices"=>{"categories"=>{"id"=>{"operation"=>categoryIDtofilter}}}}

# getting the list of packages
packages = productPackageService.object_filter(objectFilter).object_mask(objectMask).object_with_id(packageId).getItemPrices()
pp (packages)

```
