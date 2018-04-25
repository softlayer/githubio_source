---
title: "change_values_monitor_agent.rb"
description: "change_values_monitor_agent.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Monitoring_Agent"
tags:
    - "monitoring"
---


```
# Edit agent configuration values
#
# Important manual pages
# http://sldn.softlayer.com/reference/services/SoftLayer_Monitoring_Agent
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Monitoring_Agent
#
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
require 'softlayer_api'

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'

agent_id = 121_169_6

configuration_values = [
  {
    'agentId' => 121_169_6,
    'id' => 212_433_18,
    'value' => 90
  }
]

client = SoftLayer::Client.new(username: USERNAME, api_key: API_KEY)
change_monitor = client.service_named('SoftLayer_Monitoring_Agent')

begin
  result = change_monitor.object_with_id(agent_id).applyConfigurationValues(configuration_values)
  puts result
rescue StandardError => exception
  puts "Unable to edit the configuration values: #{exception}"
end

```
