---
title: "Get a list of Virtual Guests and Bare Metal servers per Pod in a Datacenter"
description: "List active Bare Metal and Virtual servers from each pod from a specific datacenter."
date: "2016-11-18"
classes: ["SoftLayer_Account"]
tags:
    - "objectMask"
    - "objectFilter"
    - "getHardware"
    - "getVirtualGuests"
---


```python
import SoftLayer
import pprint
from prettytable import PrettyTable

client = SoftLayer.Client()

# Define datacenter e.g: dal05, dal09, ams01, sao01, etc
datacenter = 'dal10'

# Declare a new API service objects for SoftLayer_Account
accountClient = client['SoftLayer_Account']

# Define objectMask and objectFilters to get additional information
objectMask = 'mask[primaryNetworkComponent[router[hostname]]]'
objectFilterBms = {"hardware": {"datacenter": {"name": {"operation": datacenter}}}}
objectFilterVsi = {"virtualGuests": {"datacenter": {"name": {"operation": datacenter}}}}

# Define array to add pods
pods = []

try:
    # Getting servers and vsis
    servers = accountClient.getHardware(mask=objectMask, filter=objectFilterBms)
    vsis = accountClient.getVirtualGuests(mask=objectMask, filter=objectFilterVsi)

    # Getting pods from servers
    for server in servers:
        if server['primaryNetworkComponent']['router']['hostname'] not in pods:
            pods.append(server['primaryNetworkComponent']['router']['hostname'])
    for vsi in vsis:
        if vsi['primaryNetworkComponent']['router']['hostname'] not in pods:
            pods.append(vsi['primaryNetworkComponent']['router']['hostname'])
    # Printing servers according pods
    for pod in pods:
        table = []
        tableDetails = PrettyTable(['POD', 'Server Id', 'Hostname', 'Domain', 'Type'])
        print("POD: %s " % pod)
        for server in servers:
            if pod in server['primaryNetworkComponent']['router']['hostname']:
                tableDetails.add_row([pod, server['id'], server['hostname'], server['domain'], 'Hardware'])
        for vsi in vsis:
            if pod in vsi['primaryNetworkComponent']['router']['hostname']:
                tableDetails.add_row([pod, vsi['id'], vsi['hostname'], vsi['domain'], 'Virtual Guest'])
        print(tableDetails)

except SoftLayer.SoftLayerAPIError as e:
    print("Error. " % (e.faultCode, e.faultString))
```

Example Output

```
POD: fcr01a.dal10
+--------------+-----------+-----------------+------------------------------+---------------+
|     POD      | Server Id |     Hostname    |            Domain            |      Type     |
+--------------+-----------+-----------------+------------------------------+---------------+
| fcr01a.dal10 |  xxxxxxx  | foundationtest0 |         vmonic.local         |    Hardware   |
| fcr01a.dal10 |  xxxxxxx  | foundationtest1 |         vmonic.local         |    Hardware   |
| fcr01a.dal10 |  xxxxxxx  | foundationtest2 |         vmonic.local         |    Hardware   |
| fcr01a.dal10 |  xxxxxxx  | foundationtest3 |         vmonic.local         |    Hardware   |
| fcr01a.dal10 |  xxxxxxx  |   sethjannygpu  |         example.com          |    Hardware   |
| fcr01a.dal10 |  xxxxxxx  |  vayatta-tester |         example.com          |    Hardware   |
| fcr01a.dal10 |  xxxxxxx  |  foundationtVW  | foundationtest.vsphere.local | Virtual Guest |
| fcr01a.dal10 |  xxxxxxx  |     jrh-oel     |         example.com          | Virtual Guest |
| fcr01a.dal10 |  xxxxxxx  |   sa.blmx.cli   |         example.com          | Virtual Guest |
+--------------+-----------+-----------------+------------------------------+---------------+
POD: fcr02a.dal10
+--------------+-----------+--------------+--------------------+---------------+
|     POD      | Server Id |   Hostname   |       Domain       |      Type     |
+--------------+-----------+--------------+--------------------+---------------+
| fcr02a.dal10 |  xxxxxxx  |  jrh-quanta  |      example.com   |    Hardware   |
| fcr02a.dal10 |  xxxxxxx  | msebastian1  |      example.com   | Virtual Guest |
| fcr02a.dal10 |  xxxxxxx  |  privdal10   |      example.com   | Virtual Guest |
| fcr02a.dal10 |  xxxxxxx  |   pubdal10   |      example.com   | Virtual Guest |
| fcr02a.dal10 |  xxxxxxx  | userdatatest |      example.com   | Virtual Guest |
+--------------+-----------+--------------+--------------------+---------------+
```
