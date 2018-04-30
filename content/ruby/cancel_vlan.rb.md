---
title: "cancel_vlan.rb"
description: "cancel_vlan.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Billing_Item"
    - "SoftLayer_Network_Vlan"
tags:
    - "vlans"
---


```
# Cancel a VLAN
#
# The script will get the Billing_Item id of the VLAN service
# then it will cancel the VLAN service
#
# Important manual pages
# http://sldn.softlayer.com/reference/services/SoftLayer_Network_Vlan
# http://sldn.softlayer.com/reference/services/SoftLayer_Network_Vlan/getObject
# http://sldn.softlayer.com/reference/services/SoftLayer_Billing_Item
# http://sldn.softlayer.com/reference/services/SoftLayer_Billing_Item/cancelService
#
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
require 'softlayer_api'
require 'pp'

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'

# The VLAN id you wish to cancel
vlan_id = 582_562
# Declaring an object mask to get the billing item information
object_mask = 'mask[id,billingItem.id]'

# Declaring the API client
client = SoftLayer::Client.new(username: USERNAME, api_key: API_KEY)
network_vlan_service = client['SoftLayer_Network_Vlan']
billing_item_service = client['SoftLayer_Billing_Item']

begin
  # Getting the Billing Item to cancel the VLAN service.
  vlan = network_vlan_service.object_mask(object_mask).object_with_id(vlan_id).getObject
  # Canceling the VLAN service.
  result = billing_item_service.object_with_id(vlan['billingItem']['id']).cancelService
  print result
rescue StandardError => exception
  puts "Unable to cancel the VLAN. : #{exception}"
end

```
