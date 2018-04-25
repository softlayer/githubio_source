---
title: "get_files.py"
description: "get_files.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Media_Transcode_Account"
tags:
    - "transcoding"
---


```
"""
Get the files in a transcode account.

Important manual pages
https://sldn.softlayer.com/reference/services/SoftLayer_Network_Media_Transcode_Account
https://sldn.softlayer.com/reference/services/SoftLayer_Network_Media_Transcode_Account/getDirectoryInformation

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer
import json

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'

# The transcode account id from where you wish to get the files.
transcodeAccountId = 1514

# Directory you wish to see. Set "in" to see the uploaded files and "out" to see the converted files
directory = "in"

# Declares the service.
client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
transcodeService = client['SoftLayer_Network_Media_Transcode_Account']

try:
    status = transcodeService.getDirectoryInformation(directory, id=transcodeAccountId)
    print(json.dumps(status, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to list the files. faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))
    exit(1)

```
