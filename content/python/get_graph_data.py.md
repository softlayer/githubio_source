---
title: "get_graph_data.py"
description: "get_graph_data.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Monitoring_Agent"
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Container_Metric_Data_Type"
tags:
    - "monitoring"
---


```
"""
Get the graph data from a monitoring agent

The script gets the CPU usage in a determinate date range
for more reference see below.

Important manual pages.
http://sldn.softlayer.com/reference/services/SoftLayer_Monitoring_Agent
http://sldn.softlayer.com/reference/services/SoftLayer_Monitoring_Agent/getGraphData

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
import SoftLayer

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'
TIMEOUT = 12000

"""
Creating an skeleton SoftLayer_Container_Metric_Data_Type object
which represent the metric data that we will get.
"""
metricDataTypes = [
    {
        "summaryType": "average",
        "keyName": "CDM_CPU_USAGE",
        "name": "cdm_cpu_usage_U3lzdGVt"
    }
]

# The start date for the graph data
starDate = "2014-09-29T01:48:08.474Z"
# The end date for the graph data
endDate = "2014-09-29T01:53:08.474Z"
"""
The agent ID from where we want to get the graph data
to get the monitor agents in your virtual guest
call the SoftLayer_Virtual_Guest::getMonitoringAgents method
"""
agentId = 1448912

client = SoftLayer.Client(username=USERNAME, api_key=API_KEY, timeout=TIMEOUT)
monitorAgentService = client['SoftLayer_Monitoring_Agent']

try:
    # calling the Softlayer_Monitoring_Agent::getGraphData method
    result = monitorAgentService.getGraphData(metricDataTypes,
                                              starDate,
                                              endDate, id=agentId)
    print(result)

except SoftLayer.SoftLayerAPIError as e:
    print("Unable to get the graph data "
          % (e.faultCode, e.faultString))
    exit(1)

```
