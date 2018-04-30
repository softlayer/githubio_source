---
title: "list_agents.py"
description: "list_agents.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_User_Customer"
    - "SoftLayer_Account"
tags:
    - "brands"
---


```
'''
List agents.

The script retrieves all the agents in a brand account.
It displays the same result like in https://agent.softlayer.com/administration/user/list

Important manual pages
http://sldn.softlayer.com/reference/services/SoftLayer_Account/getUsers
http://sldn.softlayer.com/reference/services/SoftLayer_User_Customer

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
'''

import SoftLayer.API
import json

USERNAME = 'set me'
API_KEY = 'set me'

client = SoftLayer.create_client_from_env(username=USERNAME, api_key=API_KEY)

accountService = client['SoftLayer_Account']
objectMask = "mask[id, firstName, lastName, username, email, userStatus[name]]"

try:
    result = accountService.getUsers(mask=objectMask)
    print(json.dumps(result, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to list the agents. "
          % (e.faultCode, e.faultString))

```
