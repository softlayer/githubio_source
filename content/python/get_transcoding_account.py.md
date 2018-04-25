---
title: "get_transcoding_account.py"
description: "get_transcoding_account.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
tags:
    - "transcoding"
---


```
"""
Get all transcode accounts.

Important manual pages
https://sldn.softlayer.com/reference/services/SoftLayer_Account
https://sldn.softlayer.com/reference/services/SoftLayer_Account/getTranscodeAccounts

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
accountService = client['SoftLayer_Account']

try:
    transcodeAccounts = accountService.getTranscodeAccounts()
    print(json.dumps(transcodeAccounts, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to get the transcode accounts. faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))
    exit(1)

```
