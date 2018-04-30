---
title: "list_roles.py"
description: "list_roles.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_User_Permission_Role"
tags:
    - "brands"
---


```
'''
List roles.

The script retrieves all the roles in a brand account.
It displays the same result like in https://agent.softlayer.com/administration/role/list

Important manual pages
http://sldn.softlayer.com/reference/services/SoftLayer_Account/getPermissionRoles
http://sldn.softlayer.com/reference/datatypes/SoftLayer_User_Permission_Role
http://sldn.softlayer.com/article/Object-Masks

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
'''

import SoftLayer.API
import json

USERNAME = 'set me'
API_KEY = 'set me'

client = SoftLayer.create_client_from_env(username=USERNAME, api_key=API_KEY)

accountService = client['SoftLayer_Account']
objectMask = "mask[userCount]"

try:
    result = accountService.getPermissionRoles(mask=objectMask)
    print(json.dumps(result, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to list the roles. "
          % (e.faultCode, e.faultString))

```
