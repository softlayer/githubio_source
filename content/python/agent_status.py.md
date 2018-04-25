---
title: "agent_status.py"
description: "agent_status.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
tags:
    - "monitoring"
---


```
"""
Guet the status of the monitoring agent.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/findByIpAddress
http://sldn.softlayer.com/article/object-masks

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer
import json

vsiIp = "169.45.98.148"

USERNAME = 'set me'
API_KEY = 'set me'

client = SoftLayer.Client(username=USERNAME,
                          api_key=API_KEY)
vsiService = client['SoftLayer_Virtual_Guest']

try:
    objectMask = "mask[monitoringRobot[id, robotStatus[name]], monitoringAgents[statusName, name, id], monitoringServiceEligibilityFlag, datacenter]"
    vsi = vsiService.findByIpAddress(vsiIp, mask=objectMask)
    if not vsi:
        print("There is no a vsi with the IP address: " + vsiIp)
        exit(1)
    status = {}
    status['monitoringRobotStatus'] = vsi['monitoringRobot']
    status['agents'] = vsi['monitoringAgents']
    print(json.dumps(status, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to retrieve the status: faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))
    exit(1)

```
