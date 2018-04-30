---
title: "place_order_vlan.rb"
description: "place_order_vlan.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Account"
    - "SoftLayer_Product_Package"
    - "SoftLayer_Product_Order"
    - "SoftLayer_Container_Product_Order_Network_Vlan"
tags:
    - "vlans"
---


```
# Example to create a new VLAN
# the script uses the placeOrder method to order
# a new VLAN with 32 static IP address
#
# Important manual page
# http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order
# http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder
# http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/verifyOrder
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order_Network_Vlan
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Item_Price
#
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
require 'softlayer_api'
require 'pp'

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'

# Build a skeleton SoftLayer_Container_Product_Order_Network_Vlan object
# to model the order for the new VLAN
order_data = {
  'complexType' => 'SoftLayer_Container_Product_Order_Network_Vlan',
  'location' => 'AMSTERDAM',
  'packageId' => 0,
  # Build a skeleton SoftLayer_Product_Item_Price objects. These objects contain
  # much more than Ids, but SoftLayer's ordering system only needs the price's id
  # to know what you want to order.
  # to get the list of valid prices for the package
  # use the SoftLayer_Product_Package:getItems method
  # e.g.
  # productPackageService = client['SoftLayer_Product_Package']
  # prices = productPackageService.getItems(id = packageID)
  'prices' => [
    {
      'complexType' => 'SoftLayer_Product_Item_Price',
      # The price for the new Public Network Vlan
      'id' => 201_8
    },

    {
      'complexType' => 'SoftLayer_Product_Item_Price',
      # The price for 32 Static Public IP Addresses
      'id' => 367_16
    }

  ],
  'quantity' => 1,
  'sendQuoteEmailFlag' => true,
  'name' => 'myVLANnew',
  # The router ID where the VLAN will be created
  # to get the list of routers in your account
  # use the SoftLayer_Account::getRouters method
  'routerId' => 117_960
}

# Declaring the API client
client = SoftLayer::Client.new(username: USERNAME, api_key: API_KEY)
product_order_service = client.service_named('SoftLayer_Product_Order')

begin
  # verifyOrder() will check your order for errors. Replace this with a call
  # to placeOrder() when you're ready to order. Both calls return a receipt
  # object that you can use for your records.
  # Once your order is placed it'll go through SoftLayer's approval and
  # provisioning process.
  response = product_order_service.verifyOrder(order_data)
  pp response
rescue StandardError => exception
  puts "Unable to place the order. : #{exception}"
end

```
