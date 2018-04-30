---
title: "place_order_cdn.rb"
description: "place_order_cdn.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Network_ContentDelivery_Account"
    - "SoftLayer_Product_Order"
    - "SoftLayer_Container_Product_Order_Network_ContentDelivery_Account"
tags:
    - "cdn"
---


```
# Order a new CDN account
#
# Build a SoftLayer_Container_Product_Order_Network_ContentDelivery_Account
# object for a new CDN account order and pass it to the SoftLayer_Product_Order
# API service to order it. In this script we'll order a pay as you go bandwidth
# and storage CDN account. See below for more details.
#
# Important manual pages:
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order_Network_ContentDelivery_Account
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_ContentDelivery_Account
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Item_Price
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Order/verifyOrder
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Order/placeOrder
#
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
require 'softlayer_api'
require 'pp'

# Your Softlayer API username and the key
USERNAME = 'set me'
API_KEY = 'set me'
# Declare the API client
client = SoftLayer::Client.new(username: USERNAME, api_key: API_KEY)
product_order_service = client.service_named('SoftLayer_Product_Order')

# Build a skeleton SoftLayer_Container_Product_Order_Network_ContentDelivery_Account object
# containing the order you wish to place.
order_data = {
  'complexType' => 'SoftLayer_Container_Product_Order_Network_ContentDelivery_Account',
  'packageId' => 208, # the package id to order Content Delivery Network
  # The prices to order the CDN
  'prices' => [
    {
      'complexType' => 'SoftLayer_Product_Item_Price',
      'id' => 1661 # CDN pay as you go bandwidth
    },

    {
      'complexType' => 'SoftLayer_Product_Item_Price',
      'id' => 1670 # CDN No storage (origin pull)
    }
  ],
  'quantity' => 1, # We only want 1 firewall
}

begin
  # verifyOrder() will check your order for errors. Replace this with a call to
  # placeOrder() when you're ready to order. Both calls return a receipt object
  # that you can use for your records.
  response = product_order_service.verifyOrder(order_data)
  print response
rescue StandardError => exception
  # If there was an error returned from the SoftLayer API then bomb out with the
  # error message.
  puts "Unable to place the order.  #{exception}"
end

```
