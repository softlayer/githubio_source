---
title: "get_agents.rb"
description: "get_agents.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Monitoring_Agent"
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Product_Package"
tags:
    - "monitoring"
---


```
# Example to get the agents that are running in the virtual machine.
# Also we can get the agents using the getObject method and the following mask
# mask[
#                monitoringRobot.robotStatus,
#                monitoringAgents.statusName,
#                monitoringServiceEligibilityFlag,
#                datacenter
#            ]
# then we can use the
# SoftLayer_Monitoring_Agent:getObject
# SoftLayer_Monitoring_Agent:getAvailableConfigurationValues
# SoftLayer_Monitoring_Agent:getConfigurationValues
#
# important manual pages:
# http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest
# http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/getMonitoringAgents
#
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
require 'softlayer_api'

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY  = 'set me'
ENDPOINT_URL = 'set me'

# The virtual guest you which get the monitor agents
virtual_guest_id = 527_716_8

# Declare the API client to use the SoftLayer_Product_Package API service
client = SoftLayer::Client.new(username: USERNAME, api_key: API_KEY, endpoint_url: ENDPOINT_URL)
virtual_guest_service = client.service_named('SoftLayer_Virtual_Guest')

begin
  # Gets the monitor agents
  result = virtual_guest_service.object_with_id(virtual_guest_id).getMonitoringAgents
  puts result
rescue StandardError => exception
  puts "Unable to get the monitor agents: #{exception}"
end

```
