---
title: "delete_network_notification.rb"
description: "delete_network_notification.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Network_Monitor_Version"
tags:
    - "monitoring"
---


```
# Delete network monitoring
#
# The script makes a single call to SoftLayer_Network_Monitor_Version1_Query_Host::deleteObject
# method to delete the network monitoring for more information see below
#
# Important manual pages:
# http://sldn.softlayer.com/reference/services/SoftLayer_Network_Monitor_Version1_Query_Host
# http://sldn.softlayer.com/reference/services/SoftLayer_Network_Monitor_Version1_Query_Host/deleteObject
#
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
require 'softlayer_api'
require 'pp'

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'

# The id of the Newtwork monitor you wish to delete
# To get the network monitors in the VSI use this code:
# virtual_guest_service = client.service_named('SoftLayer_Virtual_Guest')
# virtual_guest_id =  7698842
# network_monitors = virtual_guest_service.object_with_id(virtual_guest_id).getNetworkMonitors()
# print (network_monitors)
id_network_monitoring_to_delete = 177_380_7

# Declare the API client
client = SoftLayer::Client.new(username: USERNAME, api_key: API_KEY)
network_monitor_version = client.service_named('SoftLayer_Network_Monitor_Version1_Query_Host')

# Send the request to delete the object
begin
  result = network_monitor_version.object_with_id(id_network_monitoring_to_delete).deleteObject
  pp(result)
rescue StandardError => e
  puts "Unable to delete network monitoring  :-( -- #{e}"
end

```
