---
title: "add_devices_to_pool.py"
description: "add_devices_to_pool.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Network_Bandwidth_Version"
    - "SoftLayer_Hardware_Server"
tags:
    - "bandwidthpools"
---


```
"""
Add servers and VSIs to a bandwidth pool.

Important manual pages
http://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server
http://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server/findByIpAddress
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Hardware_Server
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/findByIpAddress
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_Guest
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/requestVdrContentUpdates

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer
import json

USERNAME = 'set me'
API_KEY = 'set me'

listServerIps = ["184.172.45.210", "108.168.251.167"]
listVsiIps = ["169.54.234.102"]

poolId = 234419

# Declare the API client
client = SoftLayer.create_client_from_env(username=USERNAME, api_key=API_KEY)
hardwareService = client['SoftLayer_Hardware_Server']
vsiService = client['SoftLayer_Virtual_Guest']
poolService = client['SoftLayer_Network_Bandwidth_Version1_Allotment']

try:
    hardwareToAdd = []
    hardwareToRemove = []
    cloudsToAdd = []
    cloudsToRemove = []
    for ip in listServerIps:
        server = hardwareService.findByIpAddress(ip)
        hardwareToAdd.append(server)

    for ip in listVsiIps:
        vsi = vsiService.findByIpAddress(ip)
        cloudsToAdd.append(vsi)

    result = poolService.requestVdrContentUpdates(hardwareToAdd, hardwareToRemove, cloudsToAdd, cloudsToRemove, id=poolId)
    print(json.dumps(result, sort_keys=True, indent=2, separators=(',', ': ')))

except SoftLayer.SoftLayerAPIError as e:
    print("Unable to add the devices to the pool. " % (e.faultCode, e.faultString))
    exit(1)

```
