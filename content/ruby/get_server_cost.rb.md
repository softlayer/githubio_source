---
title: "get_server_cost.rb"
description: "get_server_cost.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Hardware_Server"
tags:
    - "billing"
---


```
# Get the recurring cost of a single server or all servers on your account.
#
# Get a list of servers on a SoftLayer account along with their recurring
# monthly costs. We can get that by calling getHardware() in the
# SoftLayer_Account API service with an object mask to retrieve cost.
#
# Important manual pages
# http://sldn.softlayer.com/reference/services/SoftLayer_Account/getHardware
# http://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server/getCost
#
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
require 'softlayer_api'
require 'pp'

# Your SoftLayer API key.
USERNAME = 'set me'
API_KEY = 'set me'

# Declaring the object mask to get information about cost of the bare metal server
object_mask = 'mask(SoftLayer_Hardware_Server).cost'

# Declare the API client
client = SoftLayer::Client.new(username: USERNAME, api_ke: API_KEY)
hardware_account = client['SoftLayer_Account']

begin
  # Retrieve our account's hardware records.
  servers = hardware_account.object_mask(object_mask).getHardware
  print servers
rescue StandardError => exception
  puts "Unable to retrieve the VSIs. : #{exception}"
end

```
