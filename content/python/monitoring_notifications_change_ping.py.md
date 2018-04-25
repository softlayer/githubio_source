---
title: "monitoring_notifications_change_ping.py"
description: "monitoring_notifications_change_ping.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Monitoring_Agent"
    - "SoftLayer_Network_Monitor_Version"
tags:
    - "monitoring"
---


```
"""
Create Network Notification

The script creates a Network Notification of type  service ping
and a notify wait of 5 minutes.

Important manual pages:
http://sldn.softlayer.com/reference/services/Softlayer_Monitoring_Agent
http://sldn.softlayer.com/reference/services/SoftLayer_Monitoring_Agent/getGraphData

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
import SoftLayer

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'

# Declare the API client
client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
networkMonitorService = client['SoftLayer_Network_Monitor_Version1_Query_Host']

objectTemplate = [
    {
        "guestId": 6143038,
        "ipAddress": "10.104.50.118",
        "queryTypeId": 1,
        "responseActionId": 2,
        "waitCycles": 1
    }
]

try:
    result = networkMonitorService.createObjects(objectTemplate)
    print(result)

except SoftLayer.SoftLayerAPIError as e:
    print("Unable to create the monitor."
          % (e.faultCode, e.faultString))
    exit(1)

```
