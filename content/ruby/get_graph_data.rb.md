---
title: "get_graph_data.rb"
description: "get_graph_data.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Monitoring_Agent"
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Container_Metric_Data_Type"
tags:
    - "monitoring"
---


```
# Get the graph data from a monitoring agent
#
# The script gets the CPU usage in a determinate date range
# for more reference see below.
#
# Important manual pages.
# http://sldn.softlayer.com/reference/services/SoftLayer_Monitoring_Agent
# http://sldn.softlayer.com/reference/services/SoftLayer_Monitoring_Agent/getGraphData
#
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
require 'softlayer_api'
require 'pp'

USERNAME = 'set me'
API_KEY = 'set me'

# Creating an skeleton SoftLayer_Container_Metric_Data_Type object
# which represent the metric data that we will get.
metric_data_types = [
  {
    'summaryType' => 'average',
    'keyName' => 'CDM_CPU_USAGE',
    'name' => 'cdm_cpu_usage_U3lzdGVt'
  }
]

# The start date for the graph data
star_date = '2014-09-29T01:48:08.474Z'
# The end date for the graph data
end_date = '2014-09-29T01:53:08.474Z'
# The agent ID from where we want to get the graph data
# to get the monitor agents in your virtual guest
# call the SoftLayer_Virtual_Guest::getMonitoringAgents method
agent_id = 144_891_2

# Declare the API client
client = SoftLayer::Client.new(username: USERNAME, api_key: API_KEY)
monitor_agent_service = client.service_named('SoftLayer_Monitoring_Agent')

begin
  # Calling the Softlayer_Monitoring_Agent::getGraphData method
  result = monitor_agent_service.object_with_id(agent_id).getGraphData(metric_data_types,
                                                                       star_date, end_date)
  print(result)
rescue StandardError => e
  puts "Unable to get the graph data :-( -- #{e}"
end

```
