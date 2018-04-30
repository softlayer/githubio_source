---
title: "order_file_storage.rb"
description: "order_file_storage.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Product_Order"
    - "SoftLayer_Container_Product_Order_Network_PerformanceStorage_Nfs"
tags:
    - "filestorage"
---


```
# Order File Storage.
#
# Important manual pages:
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order_Network_PerformanceStorage_Nfs
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Item_Price
# http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/verifyOrder
# http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder
#
# @license <http://sldn.softlayer.com/article/License>
# @author SoftLayer Technologies, Inc. <sldn@softlayer.com>
require 'softlayer_api'

# Your SoftLayer API username.
USERNAME = 'set me'

# Your SoftLayer API key.
API_KEY = 'set me'

quantity = 0

# The location where our File Storage will be provisioned.
location = 'AMSTERDAM'

# The package to order file storage.
package_id = 222

# The prices of the options we wish for our File Storage
# it is required you set a storage and the IOPS.
prices = [
  { 'id' => 40_668 }, # File Storage (Performance)
  { 'id' => 40_688 }, # 20 GB Storage Space
  { 'id' => 82_453 } # 100 IOPS
]

# Configuring our template for the order.
order_template = {
  'complexType' => 'SoftLayer_Container_Product_Order_Network_PerformanceStorage_Nfs',
  'quantity' => quantity,
  'location' => location,
  'packageId' => package_id,
  'prices' => prices
}

# Creating the order service.
client = SoftLayer::Client.new(username: USERNAME, api_key: API_KEY, timeout: 600)
product_order_service = client.service_named('SoftLayer_Product_Order')

# We are calling the verifyOrder() method to verify that
# our order, when you are ready call the placeOrder() method.
begin
  receipt = product_order_service.verifyOrder(order_template)
  puts receipt
rescue StandardError => exception
  puts "There was an error in your order: #{exception}"
end

```
