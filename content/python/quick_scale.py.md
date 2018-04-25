---
title: "quick_scale.py"
description: "quick_scale.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Scale_Group"
tags:
    - "scalegroups"
---


```
"""
Quick scale.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Scale_Group
http://sldn.softlayer.com/reference/services/SoftLayer_Scale_Group/scale
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Scale_Group

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer
import json

USERNAME = 'set me'
API_KEY = 'set me'

scaleGroupId = 28660

scaleAmount = 1

client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
scaleGroupService = client['SoftLayer_Scale_Group']

try:
    result = scaleGroupService.scale(scaleAmount, id=scaleGroupId)
    print(json.dumps(result, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to scale. faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))

```
