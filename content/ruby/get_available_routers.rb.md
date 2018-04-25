---
title: "get_available_routers.rb"
description: "get_available_routers.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_DedicatedHost"
tags:
    - "dedicatedhosts"
---


```
# Get the available backend routers to order a dedicated host.
#
# Important manual pages:
# http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_DedicatedHost/getAvailableRouters
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_DedicatedHost
#
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>

require 'softlayer_api'
require 'json'

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'

# Skeleton of the dedicated host to specify datacenter and configuration sizes
template_dedicated_host = {
    :cpuCount => 56,
    :diskCapacity => 1200,
    :memoryCapacity => 242,
    :datacenter => {
        :id => 814994
    }
}

# Create a SoftLayer API client object
client = SoftLayer::Client.new(username: USERNAME, api_key: API_KEY)
service = client['SoftLayer_Virtual_DedicatedHost']

begin
  # getAvailableRouters() will get all available Hardware Routers.
  available_routers = service.getAvailableRouters template_dedicated_host

  available_routers.each do |route|
    puts JSON.generate(route)
  end

rescue StandardError => exception
  puts "Unable to get available hardware routers: #{exception}"
end

```
