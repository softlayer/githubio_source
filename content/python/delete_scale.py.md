---
title: "delete_scale.py"
description: "delete_scale.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Scale_Group"
tags:
    - "scalegroups"
---


```
"""
Delete scale group.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Scale_Group
http://sldn.softlayer.com/reference/services/SoftLayer_Scale_Group/deleteObject

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer
import json

USERNAME = 'set me'
API_KEY = 'set me'

scaleGroupId = 28660

client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
scaleGroupService = client['SoftLayer_Scale_Group']

try:
    result = scaleGroupService.deleteObject(id=scaleGroupId)
    print(json.dumps(result, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to delete the scale group. faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))

```
