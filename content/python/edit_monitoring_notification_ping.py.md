---
title: "edit_monitoring_notification_ping.py"
description: "edit_monitoring_notification_ping.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Network_Monitor_Version"
tags:
    - "monitoring"
---


```
"""
Change the basic monitoring

The script will change the configuration for a address in a virtual guest
reference pages

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Monitor_Version1_Query_Host
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Monitor_Version1_Query_Host/editObject

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
import SoftLayer

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'

# The virtual guest ID you wish change the monitoring
virtualGuestId = 6143038
# The address you wish to change
address = "10.104.50.118"

# Declare the API client
client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
virtualGuestService = client['SoftLayer_Virtual_Guest']
networkMonitorService = client['SoftLayer_Network_Monitor_Version1_Query_Host']

try:
    monitors = virtualGuestService.getNetworkMonitors(id=virtualGuestId)
    print(monitors)

except SoftLayer.SoftLayerAPIError as e:
    print("Unable to get the network monitors "
          % (e.faultCode, e.faultString))
    exit(1)

# Looking for the monitor which has desire address
for monitor in monitors:
    if monitor['ipAddress'] == address:
        # Changing the actions id
        # "id = 1" do nothing
        # "id = 2" notify users
        monitor["responseActionId"] = 1
        # changing the monitor action
        # "id = 1" service ping
        # "id = 17" slow ping
        monitor["queryTypeId"] = 17
        try:
            result = networkMonitorService.editObject(monitor, id=monitor['id'])
            print(result)
        except SoftLayer.SoftLayerAPIError as e:
            print("Unable to get the network monitors " % (e.faultCode, e.faultString))
            exit(1)

```
