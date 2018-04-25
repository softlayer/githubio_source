---
title: "get_configuration_template_monitor.rb"
description: "get_configuration_template_monitor.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Monitoring_Agent"
tags:
    - "monitoring"
---


```
# Get the configuration of a particular monitor
#
# Important manual pages.
# http://sldn.softlayer.com/reference/services/SoftLayer_Monitoring_Agent
# http://sldn.softlayer.com/reference/services/SoftLayer_Monitoring_Agent/getConfigurationTemplate
#
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
require 'softlayer_api'
require 'pp'

client = SoftLayer::Client.new(username: 'set me', api_key: 'set me')

monitor_agent_id = 108_158_4

monitor_service = client.service_named('SoftLayer_Monitoring_Agent')
object_mask = 'mask[configurationSections[subSections[definitions]]]'

begin
  # Getting the actual configuration for the monitor
  result = monitor_service.object_mask(object_mask).object_with_id(monitor_agent_id).getConfigurationTemplate
  puts result
rescue StandardError => exception
  puts "Unable to get the configuration template of the agent: #{exception}"
end

```
