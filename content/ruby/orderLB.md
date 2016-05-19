---
title: "Order a Local Load Balancer"
description: "Order a local load balancer using SoftLayer_Product_Item_Price objects"
date: "2016-05-18"
classes: ["SoftLayer_Product_Order"]
tags:
    - "placeOrder"
    - "verifyOrder"
---

```ruby

require 'rubygems'
require 'softlayer_api'

location = 'DALLAS06'

# The id of the SoftLayer_Product_Package you wish to order.
# In this case it is a Local Load Balancer.
packageId = 194

# Build a skeleton SoftLayer_Product_Item_Price objects. These objects contain
# much more than ids, but SoftLayer's ordering system only needs the price's id
# to know what you want to order.

# Every item in SoftLayer's product catalog is assigned an id. Use these ids
# to tell the SoftLayer API which options you want in your new server. Use
# the getActivePackages() method in the SoftLayer_Account API service to get
# a list of available item and price options per available package.
prices = [
   {'id' => 2078}  # Shared Load Balancer w/ 500 VIP Connections
]

# Build a skeleton SoftLayer_Container_Product_Order object
# containing the order you wish to place.
orderTemplate = {
   'location' => location,
   'packageId' => packageId,
   'prices' => prices
}

softlayer_client = SoftLayer::Client.new(:timeout => 120)

# Declare the API client to use the SoftLayer_Product_Order API service
client = softlayer_client.service_named('Product_Order')


begin
 # verifyOrder() will check your order for errors. Replace this with a call to
 # placeOrder() when you're ready to order. Both calls return a receipt object
 # that you can use for your records.
 #
 # Once your order is placed it'll go through SoftLayer's provisioning process.

 receipt = client.verifyOrder(orderTemplate)
 puts receipt
rescue Exception => exception
 puts "There is an error in the order: #{exception}"
end

```
