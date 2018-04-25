---
title: "determine_required_items.rb"
description: "determine_required_items.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Product_Package"
tags:
    - "package"
---


```
# Determine Required items
#
# Each Package is aware of a list of ItemCategories that make sense for that Package.
# This list is called the Packages "Configuration". Within the configuration,
# the Package may identify certain categories that are required, meaning you must include
# an ItemPrice from that category in any order you make against that Package
#
# Important manual pages:
# http://sldn.softlayer.com/reference/services/SoftLayer_Product_Package/getConfiguration
# http://sldn.softlayer.com/reference/services/SoftLayer_Product_Package/getItemPrices
# http://sldn.softlayer.com/article/Python
# @License: http://sldn.softlayer.com/article/License
# @Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>

require 'rubygems'
require 'softlayer_api'
require 'pp'

SL_API_USERNAME = 'set me'
SL_API_KEY = 'set me'

client = SoftLayer::Client.new(
  username: SL_API_USERNAME,
  api_key: SL_API_KEY
)
# Set the ID of the package to retrieve the information
package_id = 46

# Only retrieve the boolean to determine if this category
# is required and the category name and ID
category_object_mask = 'mask[isRequired, itemCategory[id, name]]'

# Retrieve a list of category configurations associated with our chosen package
configurations = client['Product_Package'].object_mask(category_object_mask).object_with_id(package_id).getConfiguration

# For each price we only want the id, the ID of the category(ies) it is a member of,
# and the item description
prices_object_mask = 'mask[id,item.description,categories.id]'

# Get all itemPrices for this package
prices = client['SoftLayer_Product_Package'].object_mask(prices_object_mask).object_with_id(package_id).getItemPrices

# Text format for our prettified output
header_format = "%s - %s:\n"
price_format = "    %s -- %s\n"
configurations.each do |configuration|
  # We are only concerned with required categories...
  # skip it if we do not need it!
  next if configuration['isRequired'] != 1
  printf(header_format, configuration['itemCategory']['name'], configuration['itemCategory']['id'])
  prices.each do |price|
    if price.key?('categories')
      price['categories'].each do |category|
        if category['id'] == configuration['itemCategory']['id']
          printf(price_format, price['id'], price['item']['description'])
        end
      end
    end
  end
end

```
