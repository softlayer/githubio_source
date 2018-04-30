---
title: "view_active_alarms.py"
description: "view_active_alarms.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
tags:
    - "monitoring"
---


```
"""
View active alarms of an advanced monitoring.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/findByIpAddress
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/getMonitoringActiveAlarms

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer
import json

vsiIp = "169.45.98.148"

startDate = "2000-01-01"
endDate = "2016-12-22"

USERNAME = 'set me'
API_KEY = 'set me'

client = SoftLayer.Client(username=USERNAME,
                          api_key=API_KEY)
vsiService = client['SoftLayer_Virtual_Guest']

try:
    vsi = vsiService.findByIpAddress(vsiIp)
    if not vsi:
        print("There is no a vsi with the IP address: " + vsiIp)
        exit(1)
    result = vsiService.getMonitoringActiveAlarms(startDate, endDate, id=vsi['id'])
    print(json.dumps(result, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to view the active alarms: faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))
    exit(1)

```
