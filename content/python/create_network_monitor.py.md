---
title: "create_network_monitor.py"
description: "create_network_monitor.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Monitor_Version"
tags:
    - "monitoring"
---


```
"""
Create network monitoring

The script creates a monitoring network with Service ping
in a determinate IP address

Important manual pages
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Monitor_Version1_Query_Host
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Monitor_Version1_Query_Host

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
import SoftLayer.API
from pprint import pprint as pp

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'


# The ID of the server you wish to monitor
serverId = 7698842

"""
ID of the query type which can be found with SoftLayer_Network_Monitor_Version1_Query_Host_Stratum/getAllQueryTypes.
This example uses SERVICE PING: Test ping to address, will not fail on slow server response due to high latency or
high server load
"""
queryTypeId = 1

# IP address on the previously defined server to monitor
ipAddress = '10.104.50.118'

# Declare the API client
client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
networkMonitorVersion = client['SoftLayer_Network_Monitor_Version1_Query_Host']

# Define the SoftLayer_Network_Monitor_Version1_Query_Host templateObject.
newMonitor = {
    'guestId': serverId,
    'queryTypeId': queryTypeId,
    'ipAddress': ipAddress
}

# Send the request for object creation and display the return value
try:
    result = networkMonitorVersion.createObject(newMonitor)
    pp(result)
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to create new network monitoring "
          % (e.faultCode, e.faultString))
    exit(1)

```
