---
title: "bypass_vlans.rb"
description: "bypass_vlans.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Gateway"
tags:
    - "gateway"
---


```
#
# Bypass the vlans in a gateway device.
#
# Important manual pages:
# http://sldn.softlayer.com/reference/services/SoftLayer_Network_Gateway/getInsideVlans
# http://sldn.softlayer.com/reference/services/SoftLayer_Network_Gateway/bypassVlans
# http://sldn.softlayer.com/article/Object-Filters
#
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
#

require 'softlayer_api'

# Your SoftLayer API key and username.
USERNAME = 'set me'
API_KEY = 'set me'

gateway_id = 615_22
vlan_ids_to_remove = [108_432_5, 865_555]

client = SoftLayer::Client.new(username: USERNAME, api_key: API_KEY)
gateway_service = client.service_named('SoftLayer_Network_Gateway')
object_filter = SoftLayer::ObjectFilter.new
object_filter.set_criteria_for_key_path('insideVlans.networkVlanId',     'operation' => 'in',
                                                                         'options' => [{
                                                                           'name' => 'data',
                                                                           'value' => vlan_ids_to_remove
                                                                         }])

begin
  gateway_vlans = gateway_service.object_with_id(gateway_id).object_filter(object_filter).getInsideVlans
  result = gateway_service.object_with_id(gateway_id).bypassVlans(gateway_vlans)
  puts result
 rescue StandardError => exception
  puts "Unable to bypass the VLANs.  #{exception}"
end

```
