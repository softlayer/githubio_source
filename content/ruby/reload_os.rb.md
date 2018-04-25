---
title: "reload_os.rb"
description: "reload_os.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Hardware_Server"
tags:
    - "baremetalservers"
---


```
# Reload servers from a list of IPs
#
# This script looks for a server with a determinate IP address and reloads
# the Operative System with another one.
# It makes a single call to the reloadOperatingSystem() method in the
# SoftLayer_Hardware_Server API service
#
# Important manual pages
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Hardware_Server
# http://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server/findByIpAddress
# http://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server/reloadOperatingSystem
#
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
require 'softlayer_api'
require 'pp'

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'

# The IP addresses you wish to reload
ips_to_reload = ['1.1.1.1', '2.2.2.2']

# The new OS you wish to load
new_os_to_load = 'CentOS 5.x - Minimal Install (64 bit)'

# Declare a new API service objects for:
# SoftLayer_Hardware_Server
client = SoftLayer::Client.new(username: USERNAME, api_key: API_KEY)
hardware_service = client.service_named('SoftLayer_Hardware_Server')

# Add an object mask to retrieve our prices related to the servers
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Hardware_Server
# for a list of the relational properties you can retrieve along with hardware.
object_mask = 'mask[billingItem[package[items[prices]]]]'

# The list of servers to reload
servers_to_reload = {}

# We are looking for the server with the specified IP addresses
# and the price for the new OS to load
ips_to_reload.each do |ip_to_reload|
  server = hardware_service.object_mask(object_mask).find_by_ip_address(ip_to_reload)
  servers_to_reload[ip_to_reload] = {}
  servers_to_reload[ip_to_reload]['id'] = server['id']
  if server.key?('primaryIpAddress')
    server['billingItem']['package']['items'].each do |item|
      if item['description'] == new_os_to_load
        servers_to_reload[ip_to_reload]['priceId'] = item['prices'][0]['id']
        break
      end
    end
  end
end

# We are calling the reloadOperatingSystem for the desired servers
ips_to_reload.each do |ip_to_reload|
  config = {
    'itemPrices' => [
      {
        'id' => servers_to_reload[ip_to_reload]['priceId']
      }
    ]
  }
  reload = hardware_service.object_with_id(servers_to_reload[ip_to_reload]['id']).reloadOperatingSystem('FORCE', config)
  print reload
end

```
