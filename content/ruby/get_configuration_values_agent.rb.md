---
title: "get_configuration_values_agent.rb"
description: "get_configuration_values_agent.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Monitoring_Agent"
    - "SoftLayer_Product_Package"
tags:
    - "monitoring"
---


```
# Gets the actual monitor agent configuration
# the values can be modified and change using the SoftLayer_Monitoring_Agent::applyConfigurationValues
# 
# Important manual pages:
# http://sldn.softlayer.com/reference/services/SoftLayer_Monitoring_Agent
# http://sldn.softlayer.com/reference/services/SoftLayer_Monitoring_Agent/getConfigurationValues
#
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
require 'softlayer_api'

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'
ENDPOINT_URL = 'set me'

# The monitor agent ID you which to get the actual configuration
monitor_agent_id = 121_169_6

# Declaring the API client to use the SoftLayer_Product_Package API service
client = SoftLayer::Client.new(username: USERNAME, api_key: API_KEY, endpoint_url: ENDPOINT_URL)
monitor_service = client.service_named("SoftLayer_Monitoring_Agent")

begin
  # Getting the actual configuration for the monitor
  result = monitorService.object_with_id(monitor_agent_id).getConfigurationValues
  puts result
rescue StandardError => exception
  puts "Unable to get the configuration of the agent: #{exception}"
end

```
