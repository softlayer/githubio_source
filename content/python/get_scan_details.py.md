---
title: "get_scan_details.py"
description: "get_scan_details.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Security_Scanner_Request"
tags:
    - "vulnerabilityscan"
---


```
"""
Get Scan vulnerabilities details.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Security_Scanner_Request
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Security_Scanner_Request/getReport
"""

import SoftLayer

USERNAME = 'set me'
API_KEY = 'set me'

# The scan ID you want to get the details.
scanId = 1135575

# Declares a new API service object.
client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
networkSecurityScannerService = client['SoftLayer_Network_Security_Scanner_Request']

try:
    # Gets a report in HTML format.
    result = networkSecurityScannerService.getReport(id=scanId)
    print(result)
except SoftLayer.SoftLayerAPIError as e:
    print("Error  faultCode=%s, faultString=%s"
          % (e.faultCode, e.faultString))
    exit(1)

```
