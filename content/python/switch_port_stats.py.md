---
title: "switch_port_stats.py"
description: "switch_port_stats.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Hardware_Server"
    - "SoftLayer_Container_Network_Port_Statistic"
    - "SoftLayer_NetworkComponent"
    - "SoftLayer_Account"
    - "SoftLayer_Network_Component"
tags:
    - "vlans"
---


```
"""
Retrieve a list of switch port statistics for a server's network interfaces.

This script makes a single call to the getPortStatistics() method in the
SoftLayer_Network_Component API service
for each of a server's network components to query port statistics for that
interface from SoftLayer's switches. Port statistics are modeled by the
SoftLayer__Container_Network_Port_Statistic data type
See below for more details.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_NetworkComponent/getPortStatistics
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Network_Port_Statistic

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
import SoftLayer.API
from pprint import pprint as pp

# Your SoftLayer API key and username.
USERNAME = 'set me'
API_KEY = 'set me'

"""
Your server's id. Call the getHardware() method in the SoftLayer_Account API
service (http://sldn.softlayer.com/reference/services/SoftLayer_Account/getHardware)
to get a list of your account's hardware records.
"""
serverId = 87165

# Declaring the API client
client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
hardwareServerService = client['SoftLayer_Hardware_Server']
networkComponentService = client['SoftLayer_Network_Component']

"""
Switching port statistics are measured off the server's network components. Use
an object mask to network component records along with our server record.
"""
objectMask = "mask[networkComponents]"

try:
    """
    Making the call to retrieve our hardware record. Once we have that we can query
    the server's network components.
    """
    server = hardwareServerService.getObject(mask=objectMask, id=serverId)
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to retrieve server record. "
          % (e.faultCode, e.faultString))
    exit(1)

# Separating our network components for easier processing later.
networkComponents = server['networkComponents']
# Print out a simple report header.
pp("Switchport statistics for " + server['fullyQualifiedDomainName'])

"""
Loop through our server's network components. For each NIC make a call to the
SoftLayer_Network_Component API service method getPortStatics() to get a list
of switchport statistics retrieved from the switch on the other side of your
NIC. Print a simple report per NIC.
"""
for networkComponent in networkComponents:
    # Skip the management network component.
    if networkComponent['name'] != 'mgmt':
        try:
            # Retrieve switchport statistics for the NIC.
            stats = networkComponentService.getPortStatistics(id=networkComponent['id'])
            pp(stats)
        except SoftLayer.SoftLayerAPIError as e:
            print("Unable to retrieve switchport statics for . " + networkComponent['name'] + networkComponent['port'] % (e.faultCode, e.faultString))
            exit(1)

```
