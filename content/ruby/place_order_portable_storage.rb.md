---
title: "place_order_portable_storage.rb"
description: "place_order_portable_storage.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Container_Product_Order_Virtual_Disk_Image"
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Product_Package"
    - "SoftLayer_Product_Order"
tags:
    - "portablestorages"
---


```
# Order a portal storage
#
# The script orders a portable storage, it makes a single call to the
# SoftLayer_Product_Order::placeOrder method.
#
# Important manual pages
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order_Virtual_Disk_Image
# http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order
# http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Item_Price
#
require 'softlayer_api'
require 'pp'

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'

# Building an skeleton SoftLayer_Container_Product_Order_Virtual_Disk_Image to the order
order_template = {
  'complexType' => 'SoftLayer_Container_Product_Order_Virtual_Disk_Image',
  'location' => 'SANJOSE',
  # The package for order portable storage
  'packageId' => 198,
  'diskDescription' => 'test portable storage',
  'prices' => [
    {
      # The prices for the portable storage
      # to see the list of prices available for the package
      # use the Softlayer_Product_Package::getItems method (http://sldn.softlayer.com/reference/services/SoftLayer_Product_Package/getItems)
      # e.g.
      # client = SoftLayer::Client.new(:username => user,:api_key => api_key)
      # productPackageService = client.service_named("Softlayer_Product_Package")
      # packageID = 198
      # result = productPackageService.object_with_id(packageID).getItems()
      'id' => 218_61,
      'complexType' => 'SoftLayer_Product_Item_Price'
    }
  ]
}

# Declaring the API client to use the SoftLayer_Product_Order API service
client = SoftLayer::Client.new(username: USERNAME, api_key: API_KEY)
product_order_service = client.service_named('SoftLayer_Product_Order')

begin
  # Verifies the order when you are ready to create the
  # portal storage replace "verifyOrder" by "placeOrder"
  result = product_order_service.verifyOrder(order_template)
  pp result
rescue StandardError => exception
  # If there was an error returned from the SoftLayer API then bomb out with the
  # error message.
  puts "Unable to place the order.  #{exception}"
end

```
