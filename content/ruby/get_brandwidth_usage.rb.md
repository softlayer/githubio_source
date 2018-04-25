---
title: "get_brandwidth_usage.rb"
description: "get_brandwidth_usage.rb"
date: "2018-04-25"
classes: 
    - "SoftLayer_Hardware_Server"
tags:
    - "baremetalservers"
---


```
#
# Retrieve a bandwidth usage for a list of servers.
#
# Retrieve a bandwidth usage for a list of servers.
# It makes a single call to the Softlayer_Hardware_Server::getObject method  
# For more information see below.
#
# Important manual pages
# http://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server/getObject
# http://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Hardware_Server
#
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc.<sldn@softlayer.com>
require 'softlayer_api'
require 'pp'

# Your SoftLayer username and API key.
USERNAME = ''
API_KEY = 'apikey_goes_here'

# The list of server that wish to see the bandwidth usage
server_ids = [153_851, 166_391]

client = SoftLayer::Client.new(username: USERNAME, api_key: API_KEY)
hardware_server_service = client.service_named('Hardware_Server')

# Add an object mask to retrieve our hardware' related items such as its
# host name and currentBillableBandwidthUsage. Object masks
# can retrieve any information related to your object. See
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Hardware_Server
# for a list of the relational properties you can retrieve along with hardware.
object_mask = 'mask[hostname,currentBillableBandwidthUsage]'

total = 0.0
server_ids.each do |server_id|
  bandwidth_data = hardware_server_service.object_with_id(server_id).object_mask(object_mask).getObject
  pp bandwidth_data['hostname'] + ': ' + (bandwidth_data['currentBillableBandwidthUsage'].to_f).to_s + 'GB'
  total += bandwidth_data['currentBillableBandwidthUsage'].to_f
end

pp 'Total :' + total.to_s + 'GB'

```
