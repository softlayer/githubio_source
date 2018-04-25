---
title: "place_order_nas.rb"
description: "place_order_nas.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Container_Product_Order_Network_Storage_Nas"
    - "SoftLayer_Product_Order"
tags:
    - "nas"
---


```
# Order a NAS
#
# Build a SoftLayer_Container_Product_Order_Network_Storage_Nas
# object for a new CDN account order and pass it to the SoftLayer_Product_Order
# API service to order it. In this script we'll order a NAS. See below for more details.
#
# Important manual pages:
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order_Network_Storage_Nas
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Item_Price
# http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/verifyOrder
# http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder
#
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>

require 'softlayer_api'
require 'pp'

USERNAME = 'set me'
API_KEY = 'set me'

# Building a skeleton SoftLayer_Container_Product_Order_Network_Storage_Nas object
# containing the order you wish to place.
order_data = {
  'complexType' => 'SoftLayer_Container_Product_Order_Network_Storage_Nas',

  'packageId' => 216, # the package id to order NAS
  'location' => 'AMSTERDAM',
  # The prices to order the NAS
  'prices' => [
    {
      'complexType' => 'SoftLayer_Product_Item_Price',
      'id' => 508 # 20 GB NAS
    }

  ],
  'quantity' => 1,
  'privateCloudOrderFlag' => false
}

# Declaring the API client
client = SoftLayer::Client.new(username: USERNAME, api_key: API_KEY)
product_order_service = client.service_named('SoftLayer_Product_Order')

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
