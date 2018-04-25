---
title: "associate_vlan.rb"
description: "associate_vlan.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Gateway_Vlan"
tags:
    - "gateway"
---


```
#
# Associate vlans in a gateway device.
#
# Important manual pages:
# http://sldn.softlayer.com/reference/services/SoftLayer_Network_Gateway_Vlan/createObjects
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Gateway_Vlan/
#
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>

# Your SoftLayer API key and username.

require 'softlayer_api'
require 'json'

USERNAME = 'set me'
API_KEY = 'set me'

gateway_id = 615_22
vlan_id_to_add = 108_432_5

# Declaring the API client
client = SoftLayer::Client.new(username: USERNAME, api_key: API_KEY)
gateway_vlan_service = client.service_named('SoftLayer_Network_Gateway_Vlan')

object = {
  'bypassFlag' => false,
  'networkGatewayId' => gateway_id,
  'networkVlanId' => vlan_id_to_add
}

template = Array.new()
template.push(object)

begin
  result = gateway_vlan_service.createObjects(template)
  puts JSON.pretty_generate(result)
rescue StandardError => exception
  puts "Unable to associate VLAN. : #{exception}"
end
```
