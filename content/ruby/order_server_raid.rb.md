---
title: "order_server_raid.rb"
description: "order_server_raid.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Container_Product_Order"
    - "SoftLayer_Hardware_Server"
    - "SoftLayer_Product_Order"
tags:
    - "baremetalservers"
---


```
# Order a server with RAID.
#
# The script orders a server wich contains a RAID configuration.
# For more information see below.
#
# Important manual pages:
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Hardware_Server
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Item_Price
# http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/verifyOrder
# http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder
#
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
require 'softlayer_api'
require 'pp'

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY  = 'set me'

# Declaring the API client
client = SoftLayer::Client.new(username: USERNAME, api_key: API_KEY)
product_order_service = client.service_named('SoftLayer_Product_Order')

product_order = {
  'orderContainers' => [
    {
      'hardware' => [
        {
          'domain' => 'imdemocloud.com',
          'hostname' => 'sl-provisioner-node'
        }
      ],
      'sshKeys' => [{ 'sshKeyIds' => [13_101] }],
      'location' => 265_592,
      'packageId' => 158,
      'prices' => [
        { 'id' => 35_323 },
        { 'id' => 30_308 },
        { 'id' => 25_663 },
        { 'id' => 27_597 },
        { 'id' => 33_867 },
        { 'id' => 25_014 },
        { 'id' => 34_807 },
        { 'id' => 27_023 },
        { 'id' => 32_627 },
        { 'id' => 32_500 },
        { 'id' => 33_483 },
        { 'id' => 35_310 },
        { 'id' => 24_259 },
        { 'id' => 24_259 },
        { 'id' => 30_728 },
        { 'id' => 30_728 },
        { 'id' => 30_728 },
        { 'id' => 30_728 },
        { 'id' => 30_728 },
        { 'id' => 30_728 },
        { 'id' => 30_728 },
        { 'id' => 30_728 },
        { 'id' => 30_728 },
        { 'id' => 30_728 },
        { 'id' => 30_728 },
        { 'id' => 30_728 },
        { 'id' => 30_728 },
        { 'id' => 30_728 },
        { 'id' => 30_728 },
        { 'id' => 30_728 },
        { 'id' => 33_644 },
        { 'id' => 36_037 }
      ],
      'primaryDiskPartitionId' => 1,
      'quantity' => 1,
      'storageGroups' => [
        {
          'arraySize' => 2000,
          'arrayTypeId' => 2,
          'hardDrives' => [
            0, 1
          ],
          'partitionTemplateId' => 1
        },
        {
          'arraySize' => 32_000,
          'arrayTypeId' => 5,
          'hardDrives' => [
            2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17
          ]
        }
      ]
    }
  ]
}

begin
  result = product_order_service.placeOrder(product_order)
  pp result
rescue StandardError => exception
  puts "There was an error in your order: #{exception}"
end

```
