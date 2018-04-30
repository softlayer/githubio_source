---
title: "create_network_monitor.rb"
description: "create_network_monitor.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Monitor_Version"
tags:
    - "monitoring"
---


```
# Create network monitoring
#
# The script creates a monitoring network with Service ping
# in a determinate IP address
#
# Important manual pages
# http://sldn.softlayer.com/reference/services/SoftLayer_Network_Monitor_Version1_Query_Host
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Monitor_Version1_Query_Host
#
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
require 'softlayer_api'
require 'pp'

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'

# The ID of the server you wish to monitor
server_id = 759_848_2

# Id of the query type which can be found with SoftLayer_Network_Monitor_Version1_Query_Host_Stratum/getAllQueryTypes.
# This example uses SERVICE PING: Test ping to address, will not fail on slow server response due to high latency or
# high server load
query_type_id = 1

# IP address on the previously defined server to monitor
ip_address = '10.120.63.199'

# Define the SoftLayer_Network_Monitor_Version1_Query_Host templateObject.
# the template object will create a monitoring network for a virtual guest
# to create the  the monitoring network in
# a hardware change "guestId" by "hardwareId"
new_monitor = {
  'guestId' => server_id,
  'queryTypeId' => query_type_id,
  'ipAddress' => ip_address
}

# Declare the API client
client = SoftLayer::Client.new(username: USERNAME, api_key: API_KEY)
network_monitor_version = client.service_named('SoftLayer_Network_Monitor_Version1_Query_Host')

begin
  result = network_monitor_version.createObject(new_monitor)
  pp(result)
rescue StandardError => e
  puts "Unable to create new network monitoring  :-( -- #{e}"
end

```
