---
title: "shutdown_port_disactive_port.rb"
description: "shutdown_port_disactive_port.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Hardware_Server"
tags:
    - "baremetalservers"
---


```
# Sets the networks speed for a hardware devices
#
# This script makes a single call to the setPublicNetworkInterfaceSpeed() method
# to change the speed to public network or call the setPrivateNetworkInterfaceSpeed method
# to change the speed to private network.
#
# Important manual pages
# http:'sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server/setPublicNetworkInterfaceSpeed
# http:'sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server/setPrivateNetworkInterfaceSpeed
#
# License: http:'sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
require 'softlayer_api'
require 'pp'

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'

# The ID of the hardware you wish modified the networks.
hardware_id = 167_407

# The speed you wish configure if you want to disconnect the network you should set the value to '0'
new_speed_public_network = 10
new_speed_private_network = 100

client = SoftLayer::Client.new(username: USERNAME, api_key: API_KEY)
hardware_server_service = client['SoftLayer_Hardware_Server']

begin
  # It is not possible to update the two networks at same time, you need to update one and wait until
  # the transaction is completed to update the second one.
  result = hardware_server_service.object_with_id(hardware_id).setPublicNetworkInterfaceSpeed(new_speed_public_network)
  print 'The public network speed has been modified? ' + result.to_s
  result = hardware_server_service.object_with_id(hardware_id).setPrivateNetworkInterfaceSpeed(new_speed_private_network)
  print 'The private network speed has been modified? ' + result.to_s
rescue StandardError => exception
  puts "Unable to modify networks. : #{exception}"
end

```
