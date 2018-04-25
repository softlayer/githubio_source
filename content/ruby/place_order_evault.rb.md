---
title: "place_order_evault.rb"
description: "place_order_evault.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Hardware"
    - "SoftLayer_Container_Product_Order_Network_Storage_Backup_Evault_Vault"
    - "SoftLayer_Product_Order"
    - "SoftLayer_Virtual_Guest"
tags:
    - "evault"
---


```
# Example to order an Evault.
#
# The script orders an Evault device, it makes a call to the
# SoftLayer_Product_Order::placeOrder method.
# For more information see below.
#
# Important manual pages:
# http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order_Network_Storage_Backup_Evault_Vault
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Hardware
#
# @license <http://sldn.softlayer.com/article/License>
# @author SoftLayer Technologies, Inc. <sldn@softlayer.com>
require 'rubygems'
require 'softlayer_api'
require 'pp'

# Your SoftLayer API username and key.
# Generate an API key at the SoftLayer Customer Portal:
# https://manage.softlayer.com/Administrative/apiKeychain
USERNAME = 'set me'
API_KEY = 'set me'

# Create a SoftLayer API client object
client = SoftLayer::Client.new(username: USERNAME, api_key: API_KEY)
product_order_service = client['SoftLayer_Product_Order']

order_template = {
  'complexType' => 'SoftLayer_Container_Product_Order_Network_Storage_Backup_Evault_Vault',
  # Build a skeleton SoftLayer_Hardware object.
  # The object contains the hardware ID of the
  # Bare Metal server which will contain the Evault
  # If you want use a Virtual Server instead a
  # Bare Metal server build a skeleton SoftLayer_Virtual_Guest object
  'virtualGuests' => [
    {
      'complexType' => 'SoftLayer_Virtual_Guest',
      'id' => 424_155_0
    }
  ],
  # The location for the Evault
  'location' => 'DALLAS06',
  'packageId' => 0,
  # Build a skeleton SoftLayer_Product_Item_Price object.
  # The object contains the price ID of the Evaul device
  # you wish order.
  'prices' => [
    {
      'complexType' => 'SoftLayer_Product_Item_Price',
      'id' => 1045
    }
  ],
  'quantity' => 1
}

begin
  # verifyOrder() will check your order for errors. Replace this with a call
  # to placeOrder() when you're ready to order. Both calls return a receipt
  # object that you can use for your records.
  #
  # Once your order is placed it'll go through SoftLayer's approval and
  # provisioning process.
  result = product_order_service.verifyOrder(order_template)
  print(result)
rescue => error_reason
  puts "The order could not be verified by the server #{error_reason}"
end

```
