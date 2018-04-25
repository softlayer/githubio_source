---
title: "get_transcode_jobs.py"
description: "get_transcode_jobs.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Media_Transcode_Account"
tags:
    - "transcoding"
---


```
"""
Get the transcode jobs.

Important manual pages
https://sldn.softlayer.com/reference/services/SoftLayer_Network_Media_Transcode_Account
https://sldn.softlayer.com/reference/services/SoftLayer_Network_Media_Transcode_Account/getTranscodeJobs

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer
import json

# The transcode account id from where you wish to get the jobs
transcodeAccountId = 1514

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'

# Declares the service.
client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
transcodeAccountService = client['SoftLayer_Network_Media_Transcode_Account']

# Declares a filter to get only the jobs with an arbitrary status.
objectFilter = {"transcodeStatusName": {"operation": "Complete"}}

try:
    jobs = transcodeAccountService.getTranscodeJobs(id=transcodeAccountId, filter=objectFilter)
    print(json.dumps(jobs, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to get the transcode jobs. faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))
    exit(1)

```
