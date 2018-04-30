---
title: "monitor_get_available_configuration_values.rb"
description: "monitor_get_available_configuration_values.rb"
date: "2018-04-25"
classes: 
    - "SoftLayer_Monitoring_Agent"
    - "SoftLayer_Product_Package"
tags:
    - "monitoring"
---


```
# Get the available configuration for the monitor agent
#
# Important manual pages:
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Monitoring_Agent
# http://sldn.softlayer.com/reference/services/SoftLayer_Monitoring_Agent/getAvailableConfigurationValues
#
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
require 'softlayer_api'

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'
ENDPOINT_URL = 'set me'

# Declare the API client to use the SoftLayer_Product_Package API service
client = SoftLayer::Client.new(username: USERNAME, api_key: API_KEY, endpoint_url: ENDPOINT_URL)

# The monitor agent id you wish to get the actual configuration
monitor_agent_id = 121_169_6

monitor_service = client.service_named('SoftLayer_Monitoring_Agent')

# The configuration definition id for the monitor agent
# the configuration definition id can be get
# https://SL198722:apikey_goes_here@stable.application.stagingdal0101.softlayer.local/sldn/rest/SoftLayer_Monitoring_Agent/1211696/getConfigurationTemplate?objectMask=mask[configurationSections[subSections[definitions]]]
# look for the id for the attributes ,name = Disk Profile > name = General > name = Disk Path
configuration_definition_id = 341_26

begin
  # Getting the actual configuration for the monitor
  result = monitor_service.object_with_id(monitor_agent_id).getAvailableConfigurationValues(configuration_definition_id)
  puts result
rescue StandardError => exception
  puts "Unable to get the configuration of the agent: #{exception}"
end

```
