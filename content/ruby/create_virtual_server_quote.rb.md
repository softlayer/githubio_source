---
title: "create_virtual_server_quote.rb"
description: "create_virtual_server_quote.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Container_Product_Order_Virtual_Guest"
    - "SoftLayer_Product_Order"
tags:
    - "quote"
---


```
#
# Create a quote.
# This script creates a quote based in the information provided into the
# SoftLayer_Container_Product_Order_Virtual_Guest object passing that object to
# SoftLayer_Product_Order::placeQuote method.
# Important manual pages:
# http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order
# http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeQuote/
# @License: http://sldn.softlayer.com/article/License
# @Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
#

require 'rubygems'
require 'softlayer_api'
require 'pp'

SL_API_USERNAME = 'set me'
SL_API_KEY = 'set me'

client = SoftLayer::Client.new(
  username: SL_API_USERNAME,
  api_key: SL_API_KEY)

product_order = {
  'orderContainers' => [
    {
      'complexType' => 'SoftLayer_Container_Product_Order_Virtual_Guest',
      'packageId' => 46,
      'location' => 'HONGKONG02',
      'quantity' => 1,
      'virtualGuests' => [
        {
          'hostname' => 'test',
          'domain' => 'test.com'
        }
      ],
      'prices' => [
        { 'id' => 164_0  },
        { 'id' => 164_4  },
        { 'id' => 139_38 },
        { 'id' => 220_2 },
        { 'id' => 248 },
        { 'id' => 273 },
        { 'id' => 230_2 },
        { 'id' => 55 },
        { 'id' => 58 },
        { 'id' => 420 },
        { 'id' => 418 },
        { 'id' => 21 },
        { 'id' => 57 },
        { 'id' => 905 }
      ],
      'primaryDiskPartitionId' => 1,
      'useHourlyPricing' => false
    }
  ],
  'quoteName' => 'testQuote',
  'sendQuoteEmailFlag' => true
}
# Create the quote
begin
  result = client['SoftLayer_Product_Order'].placeQuote(product_order)
  puts "The order was verified!\n"
  pp(result)
rescue => error_reason
  puts "The order could not be verified  #{error_reason}"
end

```
