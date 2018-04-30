---
title: "get_email_delivery_accounts.py"
description: "get_email_delivery_accounts.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
tags:
    - "emaildelivery"
---


```
"""
Get email delivery accounts.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Account
http://sldn.softlayer.com/reference/services/SoftLayer_Account/getNetworkMessageDeliveryAccounts

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer.API
import json

USERNAME = 'set me'
API_KEY = 'set me'

client = SoftLayer.create_client_from_env(username=USERNAME, api_key=API_KEY)
accountService = client['SoftLayer_Account']

objectFilter = {"type": {"keyName": {"operation": "EMAIL"}}}

try:
    result = accountService.getNetworkMessageDeliveryAccounts(filter=objectFilter)
    print(json.dumps(result, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to get the email delivery accounts faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))
    exit(1)

```
