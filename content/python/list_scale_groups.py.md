---
title: "list_scale_groups.py"
description: "list_scale_groups.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Scale_Group"
tags:
    - "scalegroups"
---


```
"""
List the scale groups in the account.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Account
http://sldn.softlayer.com/reference/services/SoftLayer_Account/getScaleGroups
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Scale_Group

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer
import json

USERNAME = 'set me'
API_KEY = 'set me'

# Create a SoftLayer API client object
client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
accountService = client['SoftLayer_Account']

objectMask = "mask[id, name, status[name, keyName], regionalGroup[id, name, description]]"

try:
    scaleGroups = []
    result = accountService.getScaleGroups(mask=objectMask)
    for item in result:
        scaleGroup = {}
        scaleGroup['id'] = item['id']
        scaleGroup['name'] = item['name']
        scaleGroup['status'] = item['status']['name']
        scaleGroup['region'] = item['regionalGroup']['name']
        scaleGroups.append(scaleGroup)
    print(json.dumps(scaleGroups, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to get the scale groups. faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))

```
