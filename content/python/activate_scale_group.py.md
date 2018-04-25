---
title: "activate_scale_group.py"
description: "activate_scale_group.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Scale_Group"
tags:
    - "scalegroups"
---


```
"""
Activate a scale group.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Scale_Group
http://sldn.softlayer.com/reference/services/SoftLayer_Scale_Group/editObject
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Scale_Group

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

template = {
    "id": scaleGroupId,
    "suspendedFlag": False
}

try:
    result = scaleGroupService.editObject(template, id=scaleGroupId)
    print(json.dumps(result, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to activate the scale group. faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))

```
