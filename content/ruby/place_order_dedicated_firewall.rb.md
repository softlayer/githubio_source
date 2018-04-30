---
title: "place_order_dedicated_firewall.rb"
description: "place_order_dedicated_firewall.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Container_Product_Order_Network_Protection_Firewall_Dedicated"
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Container_Product_Order_Network_Protection_Firewall"
    - "SoftLayer_Product_Order"
    - "SoftLayer_Product_Item_Price"
tags:
    - "dedicatedfirewall"
---


```
# Order dedicated FireWalls
#
# Important manual pages:
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order_Network_Protection_Firewall_Dedicated
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Item_Price
# http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/verifyOrder
# http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder
#
# @license <http://sldn.softlayer.com/article/License>
# @author SoftLayer Technologies, Inc. <sldn@softlayer.com>
require 'softlayer_api'

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'

# Build a skeleton SoftLayer_Container_Product_Order_Network_Protection_Firewall_Dedicated object
# containing the order you wish to place.
order_data = {
  'complexType' => 'SoftLayer_Container_Product_Order_Network_Protection_Firewall',
  'virtualGuests' => [
    {
      'complexType' => 'SoftLayer_Virtual_Guest',
      'id' => 667_410_0 # The virtual Guest ID where you wish add a fireWall.
    }
  ],
  'location' => 168_642, # The location for the fireWall in this case "San Jose 1"
  'packageId' => 0, # The package id to order fireWalls
  # The prices to order the FireWall
  'prices' => [
    {
      'complexType' => 'SoftLayer_Product_Item_Price',
      'id' => 410 # Price to 10Mbps Hardware FireWall
    }
  ],
  'quantity' => 1, # We only want 1 fireWall
}

# Declare the API client
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
