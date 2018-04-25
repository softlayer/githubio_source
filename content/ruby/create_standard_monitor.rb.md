---
title: "create_standard_monitor.rb"
description: "create_standard_monitor.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Product_Package"
    - "SoftLayer_Network_Monitor_Version"
tags:
    - "monitoring"
---


```
# Add standard monitor
#
# Important manual pages:
# http://sldn.softlayer.com/reference/services/SoftLayer_Network_Monitor_Version1_Query_Host
# http://sldn.softlayer.com/reference/services/SoftLayer_Network_Monitor_Version1_Query_Host/createObjects
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Monitor_Version1_Query_Host
#
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
require 'softlayer_api'

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'
ENDPOINT_URL = 'set me'

# Build a skeleton SoftLayer_Network_Monitor_Version1_Query_Host object
# containing the order you wish to place.
template_objects = [
  {
    'complexType' => 'SoftLayer_Network_Monitor_Version1_Query_Host',
    'arg1Value' => 'Domain', # The parameter
    'guestId' => 490_544_2, # The guest ID where you want add standard monitor
    'ipAddress' => '10.64.47.19', # The IP address of the machine
    'queryTypeId' => 17,   # 1: Service Ping 17: Slow Ping
    'responseActionId' => 2, # 1: do nothing 2:notify users
    'waitCycles' => 5 # 0: 0m, 1: 5m, 2: 10m, 3: 15m, 4: 20m, 5: 25m, 6: 30m, 7: 35m, 8: 40m, 9: 45m, 10: 45m, 11: 50m, 12: 55m, 13: 60m
  }
]

# Declare the API client to use the SoftLayer_Product_Package API service
client = SoftLayer::Client.new(username: USERNAME, api_key: API_KEY, endpoint_url: ENDPOINT_URL)
network_monitor_service = client.service_named('SoftLayer_Network_Monitor_Version1_Query_Host')

begin
  result = network_monitor_service.createObjects(template_objects)
  puts result
rescue StandardError => exception
  puts "Unable to create standard monitor: #{exception}"
end

```
