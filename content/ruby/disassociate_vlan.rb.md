---
title: "disassociate_vlan.rb"
description: "disassociate_vlan.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Gateway"
    - "SoftLayer_Network_Gateway_Vlan"
tags:
    - "gateway"
---


```
#
# Disassociate vlans in a gateway device.
#
# Important manual pages:
# http://sldn.softlayer.com/reference/services/SoftLayer_Network_Gateway_Vlan/deleteObject
# http://sldn.softlayer.com/reference/services/SoftLayer_Network_Gateway/getInsideVlans
# http://sldn.softlayer.com/article/Object-Filters
#
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>

require 'softlayer_api'

# Your SoftLayer API key and username.
USERNAME = 'set me'
API_KEY = 'set me'

gateway_id = 615_22
vlan_id_to_remove = 105_426_5

client = SoftLayer::Client.new(username: USERNAME, api_key: API_KEY)
gateway_service = client.service_named('SoftLayer_Network_Gateway')
gateway_vlan_service = client['SoftLayer_Network_Gateway_Vlan']

object_filter = SoftLayer::ObjectFilter.new { |f| f.accept('insideVlans..networkVlanId').when_it is(vlan_id_to_remove) }

begin
  gateway_vlan = gateway_service.object_with_id(gateway_id).object_filter(object_filter).getInsideVlans
  if gateway_vlan.length == 0
    print 'The configured Vlan id is not associated to the configured gateway id'
    exit
  end
  result = gateway_vlan_service.object_with_id(gateway_vlan[0]['id']).deleteObject
  puts result
 rescue StandardError => exception
  puts "Unable to remove VLAN.  #{exception}"
end

```
