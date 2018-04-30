---
title: "get_subnets.rb"
description: "get_subnets.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Subnet"
    - "SoftLayer_Network_Vlan"
tags:
    - "vlans"
---


```
# Retrieve the subnets for a VLAN
#
# Retrieve all the subnets for a determinate VLAN
# associated with a SoftLayer customer account
# We do this with a call to the getSubnets() method in the
# SoftLayer_Network_Vlan API service. See below for more details.
#
# Important manual pages:
# http://sldn.softlayer.com/reference/services/SoftLayer_Network_Vlan
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Subnet
# http://sldn.softlayer.com/reference/services/SoftLayer_Network_Vlan/getSubnets
#
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
require 'softlayer_api'
require 'pp'

# Your SoftLayer API key and username.
USERNAME = 'set me'
API_KEY = 'set me'

# The VLAN id you wish to see its subnets
vlan_id = 557_984

# Declaring the API client
client = SoftLayer::Client.new(username: USERNAME, api_key: API_KEY)
network_vlan_service = client['SoftLayer_Network_Vlan']

begin
  # Sending the request to get the subnets
  result = network_vlan_service.object_with_id(vlan_id).getSubnets
  print result
rescue StandardError => exception
  puts "Unable to retrieve the subnets. : #{exception}"
end

```
