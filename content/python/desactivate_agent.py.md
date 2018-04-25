---
title: "desactivate_agent.py"
description: "desactivate_agent.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Monitoring_Agent"
    - "SoftLayer_Virtual_Guest"
tags:
    - "monitoring"
---


```
"""
Desactive an agent.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/findByIpAddress
http://sldn.softlayer.com/reference/services/SoftLayer_Monitoring_Agent/deactivate
http://sldn.softlayer.com/article/object-masks

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer
import json

vsiIp = "169.45.98.148"
agentName = "DHCP Response Monitoring Agent"

USERNAME = 'set me'
API_KEY = 'set me'

client = SoftLayer.Client(username=USERNAME,
                          api_key=API_KEY)
vsiService = client['SoftLayer_Virtual_Guest']
agentService = client['SoftLayer_Monitoring_Agent']

try:
    objectMask = "mask[monitoringRobot[id, robotStatus[name]], monitoringAgents[statusName, name, id], monitoringServiceEligibilityFlag, datacenter]"
    vsi = vsiService.findByIpAddress(vsiIp, mask=objectMask)
    if not vsi:
        print("There is no a vsi with the IP address: " + vsiIp)
        exit(1)
    agent = {}
    for agents in vsi['monitoringAgents']:
        if agents['name'].strip().upper() == agentName.strip().upper():
            agent = agents
            break
    if not 'id' in agent:
        print("The VSI does not have a monitor agent with the name: " +  agentName)
        exit(1)
    result = agentService.deactivate(id=agent['id'])
    print(json.dumps(result, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to deactivate the monitor agent: faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))
    exit(1)

```
