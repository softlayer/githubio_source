---
title: "set_metadata_service_order.rb"
description: "set_metadata_service_order.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Product_Order"
tags:
    - "virtualservers"
---


```
# Create VSI with metadata.
#
# Important manual pages:
# https://sldn.softlayer.com/reference/services/SoftLayer_Product_Order
# https://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder
#
# @license <http://sldn.softlayer.com/article/License>
# @author SoftLayer Technologies, Inc. <sldn@softlayer.com>
require 'softlayer_api'
require 'pp'

USERNAME = 'set me'
API_KEY = 'set me'
ENDPOINT = 'set me'

client = SoftLayer::Client.new(endpoint_url: ENDPOINT, username: USERNAME, api_key: API_KEY)

server_order = SoftLayer::VirtualServerOrder.new(client)
server_order.hostname = 'server1'
server_order.domain = 'ruby-api-test.org'

server_order.datacenter = 'dal06'
server_order.cores = 2
server_order.memory = 2
server_order.os_reference_code = 'CENTOS_6_64'
server_order.max_port_speed = SoftLayer::VirtualServerOrder.max_port_speed_options(client).max
server_order.user_metadata = 'key=value
key2=value2
key3=value3
key4=value4'

begin
  result = server_order.place_order!
  pp result
rescue StandardError => exception
  puts "Unable to place the order: #{exception}"
end

```
