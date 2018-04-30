---
title: "set_restrict_access_to_ip.py"
description: "set_restrict_access_to_ip.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_User_Customer"
    - "SoftLayer_Account"
tags:
    - "users"
---


```
"""
Set restrict access to IP address.

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
    # Set the value to "" to delete the previous configured IP address.
    users[0]['ipAddressRestriction'] = "10.2.32.4"
    result = userService.editObject(users[0], id=users[0]['id'])
    print(json.dumps(result, sort_keys=True, indent=2, separators=(',', ': ')))

except SoftLayer.SoftLayerAPIError as e:
    print("Unable to set restrict access to IP address. faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))

```
