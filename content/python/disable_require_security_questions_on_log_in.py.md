---
title: "disable_require_security_questions_on_log_in.py"
description: "disable_require_security_questions_on_log_in.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_User_Customer"
    - "SoftLayer_Account"
tags:
    - "users"
---


```
"""
Disable require security questions on log in.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Account/getUsers
http://sldn.softlayer.com/reference/services/SoftLayer_User_Customer/editObject
http://sldn.softlayer.com/article/Object-Filters

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer
import json

USERNAME = 'set me'
API_KEY = 'set me'

userName = "myusernaetest0235"

client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
accountService = client['SoftLayer_Account']
userService = client['SoftLayer_User_Customer']

objectFilterUser = {"users": {"username": {"operation": userName}}}

try:
    users = accountService.getUsers(filter=objectFilterUser)
    users[0]['secondaryLoginRequiredFlag'] = False
    result = userService.editObject(users[0], id=users[0]['id'])
    print(json.dumps(result, sort_keys=True, indent=2, separators=(',', ': ')))

except SoftLayer.SoftLayerAPIError as e:
    print("Unable to disable require security questions on log in. faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))

```
