---
title: "create_job.py"
description: "create_job.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Media_Transcode_Account"
tags:
    - "transcoding"
---


```
"""
Create a transcode job.

Important manual pages
https://sldn.softlayer.com/reference/services/SoftLayer_Network_Media_Transcode_Account
https://sldn.softlayer.com/reference/services/SoftLayer_Network_Media_Transcode_Account/createTranscodeJob

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer
import json

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'

# The transcode account id.
transcodeAccountId = 1514

# The file you wish to convert.
inputFile = "/in/535fec1f9828a535fe7e06697evideo1.avi"

outputFile = "/out/myconvertedFile"

# Name of the job.
name = "testrc"

autoDeleteDuration = 259200

# The output format.
transcodePresetGuid = "{6DFA4D0A-D5C5-4E96-A7A6-21FFF3E0A9F4}"

job = {
    "inputFile": inputFile,
    "name": name,
    "outputFile": outputFile,
    "autoDeleteDuration": autoDeleteDuration,
    "transcodePresetGuid": transcodePresetGuid
}

# Declares the service.
client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
transcodeService = client['SoftLayer_Network_Media_Transcode_Account']

try:
    job = transcodeService.createTranscodeJob(job, id=transcodeAccountId)
    print(json.dumps(job, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to create the job. faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))
    exit(1)

```
