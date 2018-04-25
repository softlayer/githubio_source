---
title: "order_dedicated_host.rb"
description: "order_dedicated_host.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Product_Package"
    - "SoftLayer_Container_Product_Order"
    - "SoftLayer_Product_Order"
    - "SoftLayer_Hardware_Server"
tags:
    - "dedicatedhosts"
---


```
# Order Dedicated Hosts.
#
# Important manual pages:
# http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order
# http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/verifyOrder
# http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder
# http://sldn.softlayer.com/reference/services/SoftLayer_Product_Package
# http://sldn.softlayer.com/reference/services/SoftLayer_Product_Package/getItemPrices
#
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>

require 'softlayer_api'
require 'json'

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'

# Declare the location, packageId and quantity for the server you wish to order.
# Take account that you can only order two dedicated host at same time.
location = 'MEXICO'
packageId = 813
quantity = 2

# Skeleton of SoftLayer_Hardware_Server object to model the hostname,
# domain and the router that we want for our dedicated host.
hardware = [
    {
        :domain => 'softlayer.com',
        :hostname => 'dedicated-hostA',
        :primaryBackendNetworkComponent => {
            :router => { :id => 843613 }
        }
    },
    {
        :domain => 'softlayer.com',
        :hostname => 'dedicated-hostB',
        :primaryBackendNetworkComponent => {
            :router => { :id => 843613 }
        }
    }
]

# Build a skeleton SoftLayer_Product_Item_Price objects. To get the list of valid
# prices for the package use the SoftLayer_Product_Package:getItemPrices method
prices = [
    { :id => 200269 }  #  "56 Cores X 242 RAM X 1.2 TB"
]

# Build the skeleton of SoftLayer_Container_Product_Order object
# containing the order you wish to place.
template_order = {
    :orderContainers => [
        :location => location,
        :packageId => packageId,
        :hardware => hardware,
        :prices => prices,
        :quantity => quantity
    ]
}

# Create a SoftLayer API client object
client = SoftLayer::Client.new(username: USERNAME, api_key: API_KEY)
service = client['SoftLayer_Product_Order']

begin
  # Use verifyOrder() method to check for errors. Replace this with placeOrder() when
  # you are ready to order.
  receipt = service.verifyOrder template_order

  puts JSON.pretty_generate(receipt)

rescue StandardError => exception
  puts "Unable to place order: #{exception}"
end
```
