---
title: "get_scans.py"
description: "get_scans.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Network_Security_Scanner_Request"
tags:
    - "vulnerabilityscan"
---


```
"""
Get Scan vulnerabilities from a VSI.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Security_Scanner_Request
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Security_Scanner_Request/getReport
"""

import SoftLayer
import json

USERNAME = 'set me'
API_KEY = 'set me'

# The virtual guest ID you want to get the vulnerabilities scan.
virtualGuestId = 11528955

# Declares a new API service object.
client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
virtualGuestService = client['SoftLayer_Virtual_Guest']

# Declares an object mask to get information about the vulnerabilities scans in the VSI.
objectMask = "mask[securityScanRequests]"

try:
    result = virtualGuestService.getObject(id=virtualGuestId, mask=objectMask)
    print(json.dumps(result["securityScanRequests"], sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Error  faultCode=%s, faultString=%s"
          % (e.faultCode, e.faultString))
    exit(1)

```
