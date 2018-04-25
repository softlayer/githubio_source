---
title: "get_transcode_ftp_credencials.py"
description: "get_transcode_ftp_credencials.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Media_Transcode_Account"
tags:
    - "transcoding"
---


```
"""
Get FTP credentials.

Important manual pages
https://sldn.softlayer.com/reference/services/SoftLayer_Network_Media_Transcode_Account
https://sldn.softlayer.com/reference/services/SoftLayer_Network_Media_Transcode_Account/getFtpAttributes

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer
import json

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'

# The transcode account id from where you wish to get the credentials.
transcodeAccountId = 1514

# Declares the service.
client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
transcodeService = client['SoftLayer_Network_Media_Transcode_Account']

try:
    credentials = transcodeService.getFtpAttributes(id=transcodeAccountId)
    print(json.dumps(credentials, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to get the credentials. faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))
    exit(1)

```
