---
title: "get_presets.py"
description: "get_presets.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Media_Transcode_Account"
tags:
    - "transcoding"
---


```
"""
Get the presets.

Important manual pages
https://sldn.softlayer.com/reference/services/SoftLayer_Network_Media_Transcode_Account
https://sldn.softlayer.com/reference/services/SoftLayer_Network_Media_Transcode_Account/getPresets

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer
import json

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'

# The transcode account id from where you wish to get the presets.
transcodeAccountId = 1514

# Declares the service.
client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
transcodeService = client['SoftLayer_Network_Media_Transcode_Account']

try:
    presets = transcodeService.getPresets(id=transcodeAccountId)
    print(json.dumps(presets, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to get the presets. faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))
    exit(1)

```
