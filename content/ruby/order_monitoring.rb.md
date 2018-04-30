---
title: "order_monitoring.rb"
description: "order_monitoring.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Product_Order"
    - "SoftLayer_Container_Product_Order_Monitoring_Package"
    - "SoftLayer_Monitoring_Agent_Configuration_Template_Group"
tags:
    - "monitoring"
---


```
# Order a Monitoring Package
#
# Build a SoftLayer_Container_Product_Order_Monitoring_Package object for a new
# monitoring order and pass it to the SoftLayer_Product_Order API service to order it
# In this care we'll order a Basic (Hardware and OS) package with Basic Monitoring Package - Linux
# configuration for more details see below
#
# Important manual pages:
# https://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order_Monitoring_Package
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Item_Price
# http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/verifyOrder
# http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Monitoring_Agent_Configuration_Template_Group
#
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
require 'softlayer_api'

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY  = 'set me'

# Build a skeleton SoftLayer_Container_Product_Order_Monitoring_Package object
# containing the order you wish to place.
oder_template = {
  'complexType' => 'SoftLayer_Container_Product_Order_Monitoring_Package',
  'packageId' => 0, # The packageID for order monitoring packages is 0
  'prices' => [
    { 'id' => 230_2 } # This is the price for Monitoring Package - Basic ((Hardware and OS))
  ],
  'quantity' => 0,  # The quantity for order a service (in this case monitoring package) must be 0
  'sendQuoteEmailFlag' => true,
  'useHourlyPricing' => true,
  'virtualGuests' => [
    { 'id' => 490_603_4 } # The virtual guest ID where you want add the monitoring package
  ],
  'configurationTemplateGroups' => [
    { 'id' => 3 } # The templateID for the monitoring group (in this case Basic Monitoring package for Unix/Linux operating system.)
  ]
}

# Declare the API client to use the SoftLayer_Product_Order API service
client = SoftLayer::Client.new(username: USERNAME, api_key: API_KEY)
product_order_service = client.service_named('SoftLayer_Product_Order')

# verifyOrder() will check your order for errors. Replace this with a call to
# placeOrder() when you're ready to order. Both calls return a receipt object
# that you can use for your records.
#
# Once your order is placed it'll go through SoftLayer's provisioning process.
begin
  order = product_order_service.verifyOrder(oder_template)
  puts order
rescue StandardError => exception
  puts "Unable to place order: #{exception}"
end

```
