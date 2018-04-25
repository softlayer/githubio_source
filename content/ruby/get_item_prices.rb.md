---
title: "get_item_prices.rb"
description: "get_item_prices.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Product_Package"
tags:
    - "package"
---


```
# Get item prices
#
# This script will display the  general information related
# to a single SoftLayer product item price
#
# See below references for more details.
# http://sldn.softlayer.com/reference/services/SoftLayer_Product_Package/getItemPrices
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Item_Price
# @License: http://sldn.softlayer.com/article/License
# @Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>

require 'rubygems'
require 'softlayer_api'

SL_API_USERNAME = 'set me'
SL_API_KEY = 'set me'

client = SoftLayer::Client.new(
  username: SL_API_USERNAME,
  api_key: SL_API_KEY
)
# Set the ID of the package to retrieve the information
package_id = 46
# Text format for our prettified output
header_format = "%s - %s:\n"
item_format = "    %s:\n"
category_format = "         %s -- %s\n"

# Set the object mask to retrieve categories
category_object_mask = 'mask[categories]'
# Get all itemPrices for this package
prices = client['SoftLayer_Product_Package'].object_mask(category_object_mask).object_with_id(package_id).getItemPrices
prices.each do |price|
  printf(header_format, 'Product item price', price['id'])
  unless price['hourlyRecurringFee'].nil?
    printf("    %s - %s\n", 'Hourly price(hourlyRecurringFee)', price['hourlyRecurringFee'])
  end
  printf(item_format, 'Item')
  printf(category_format, price['item']['id'], price['item']['description'])
  unless price['categories'].nil?
    categories = price['categories']
    printf(item_format, 'Categories:')
    categories.each do |category|
      printf(category_format, category['id'], category['name'])
    end
  end
end

```
