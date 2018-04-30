---
title: "get_vlan_details.rb"
description: "get_vlan_details.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Subnet_IpAddress"
    - "SoftLayer_Network_Subnet"
    - "SoftLayer_Network_Vlan"
tags:
    - "vlans"
---


```
# Retrieves VLAN details such as primary router and subnet.
#
# Retrieves the primary router and subnet for a determinate VLAN
# associated with a SoftLayer customer account
# We do this with a call to the getObject() method in the
# SoftLayer_Network_Vlan API service using an object mask to retrieve
# associated subnets and primary router records. See below for more details.
#
# Important manual pages:
# http://sldn.softlayer.com/reference/services/SoftLayer_Network_Vlan
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Subnet
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Subnet_IpAddress
# http://sldn.softlayer.com/reference/services/SoftLayer_Network_Vlan/getObject
#
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
require 'softlayer_api'
require 'pp'

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'

# The VLAN id you wish to see its details
vlan_id = 557_984

# Declaring an object mask to get more information about the VLANs
# such as the primaryRouter and the subnets
object_mask = 'mask[primaryRouter, subnets[ipAddresses]]'

# Declaring the API client
client = SoftLayer::Client.new(username: USERNAME, api_key: API_KEY)
network_vlan_service = client['SoftLayer_Network_Vlan']

begin
  # Sending the request to get the VLAN
  result = network_vlan_service.object_mask(object_mask).object_with_id(vlan_id).getObject
  print result
rescue StandardError => exception
  puts "Unable to retrieve the VLAN details. : #{exception}"
end

```
