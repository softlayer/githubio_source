---
title: "re_deploy_all_agents.py"
description: "re_deploy_all_agents.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Monitoring_Agent"
    - "SoftLayer_Virtual_Guest"
tags:
    - "monitoring"
---


```
"""
Re-deploy all agents.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/findByIpAddress
http://sldn.softlayer.com/reference/services/SoftLayer_Monitoring_Agent/deployMonitoringAgent
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
agentService = client['SoftLayer_Monitoring_Agent']

try:
    objectMask = "mask[monitoringRobot[id, robotStatus[name]], monitoringAgents[statusName, name, id], monitoringServiceEligibilityFlag, datacenter]"
    vsi = vsiService.findByIpAddress(vsiIp, mask=objectMask)
    if not vsi:
        print("There is no a vsi with the IP address: " + vsiIp)
        exit(1)
    for agent in vsi['monitoringAgents']:
        configuration = agentService.getConfigurationTemplate(id=agent['id'])
        result = agentService.deployMonitoringAgent(configuration['id'], id=agent['id']) 
        print(json.dumps(result, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to re-deploy the monitor agents: faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))
    exit(1)

```
