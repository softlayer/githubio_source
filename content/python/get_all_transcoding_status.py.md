---
title: "get_all_transcoding_status.py"
description: "get_all_transcoding_status.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Media_Transcode_Job_Status"
tags:
    - "transcoding"
---


```
"""
Get all transcode statuses.

Important manual pages
https://sldn.softlayer.com/reference/services/SoftLayer_Network_Media_Transcode_Job_Status
https://sldn.softlayer.com/reference/services/SoftLayer_Network_Media_Transcode_Job_Status/getAllStatuses
https://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Media_Transcode_Job_Status

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer
import json

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'

# Declares the service.
client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
transcodeService = client['SoftLayer_Network_Media_Transcode_Job_Status']

try:
    status = transcodeService.getAllStatuses()
    print(json.dumps(status, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to get the transcode statuses. faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))
    exit(1)

```
