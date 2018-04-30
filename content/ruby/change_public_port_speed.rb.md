---
title: "change_public_port_speed.rb"
description: "change_public_port_speed.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
tags:
    - "virtualservers"
---


```
# Set Public Network Interface Speed.
# It sets the public network interface speed to the new speed.
#
# Important manual pages:
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_Guest
# http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest
# http://www.rubydoc.info/github/softlayer/softlayer-api-ruby-client/master/SoftLayer/Server#change_port_speed-instance_method
# http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/setPublicNetworkInterfaceSpeed
#
# @license <http://sldn.softlayer.com/article/License>
# @author SoftLayer Technologies, Inc. <sldn@softlayer.com>
require 'rubygems'
require 'softlayer_api'


# Set the server id that you want to change the port speed.
server_id = 11498371

# Set the new speed, It is expressed Mbps and should be 0, 10, 100, or 1000
new_speed = 10

# Your SoftLayer API username.
SL_API_USERNAME = 'set me'

# Your SoftLayer API key.
SL_API_KEY = 'set me'

softlayer_client = SoftLayer::Client.new(:username => SL_API_USERNAME ,
                                         :api_key => SL_API_KEY)

server = SoftLayer::VirtualServer.server_with_id(server_id, :client => softlayer_client)

begin
  result = server.change_port_speed(new_speed,public=true)
  puts "The public port speed was changed successfully: #{result}"
rescue Exception => e
  puts "Unable to change the public port speed: #{e}"
end
```
