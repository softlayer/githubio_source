---
title: "get_vlan.rb"
description: "get_vlan.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Network_Subnet"
    - "SoftLayer_Network_Subnet_IpAddress"
    - "SoftLayer_Network_Vlan"
tags:
    - "vlans"
---


```
# Retrieve account VLAN and subnet information.
#
# Retrieve a list of all VLANs associated with a SoftLayer customer account
# and print a simple report detailing these VLANs and the subnets assigned to
# them. We do this with a call to the getNetworkVlans() method in the
# SoftLayer_Account API service using an object mask to retrieve the VLANs'
# associated subnets and primary router records. See below for more details.
#
# Important manual pages:
# http://sldn.softlayer.com/reference/services/SoftLayer_Account
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Vlan
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Subnet
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Subnet_IpAddress
# http://sldn.softlayer.com/reference/services/SoftLayer_Account/getNetworkVlans
#
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
require 'softlayer_api'
require 'pp'

# Your SoftLayer API key and username.
USERNAME = 'set me'
API_KEY = 'set me'

# Declaring the API client
client = SoftLayer::Client.new(username: USERNAME, api_key: API_KEY)
account_service = client['SoftLayer_Account']

# Declaring an object mask to get more information about the VLANs
# such as the primaryRouter and the subnets
object_mask = 'mask[primaryRouter, subnets[ipAddresses]]'

begin
  # Send the request to get the VLANs
  result = account_service.object_mask(object_mask).getNetworkVlans
  print result
rescue StandardError => exception
  puts "Unable to retrieve the VLANs. : #{exception}"
end

```
