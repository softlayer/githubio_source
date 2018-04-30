---
title: "delete_network_notification.py"
description: "delete_network_notification.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Network_Monitor_Version"
tags:
    - "monitoring"
---


```
"""
Delete network monitoring

The script makes a single call to SoftLayer_Network_Monitor_Version1_Query_Host::deleteObject
method to delete the network monitoring for more information see below

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Monitor_Version1_Query_Host
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Monitor_Version1_Query_Host/deleteObject

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
import SoftLayer.API
from pprint import pprint as pp

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'

"""
The id of the network monitor you wish to delete
virtualGuestService = client['SoftLayer_Virtual_Guest']
virtualGuestId =  7698842
networkMonitors = virtualGuestService.getNetworkMonitors(id = virtualGuestId)
print (networkMonitors)
"""
idNetworkMonitoringToDelete = 1738019

# Declare the API client
client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
networkMonitorVersionService = client['SoftLayer_Network_Monitor_Version1_Query_Host']

# Send the request to delete the object
try:
    result = networkMonitorVersionService.deleteObject(id=idNetworkMonitoringToDelete)
    pp(result)
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to delete the network monitoring "
          % (e.faultCode, e.faultString))
    exit(1)

```
