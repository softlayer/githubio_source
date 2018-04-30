---
title: "list_customers.py"
description: "list_customers.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Brand"
tags:
    - "brands"
---


```
'''
List customers.

The script retrieves all the customers in a brand account.
It displays the same result like in https://agent.softlayer.com/customer/account/list

Important manual pages
http://sldn.softlayer.com/reference/services/SoftLayer_Brand/getOwnedAccounts
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Account
http://sldn.softlayer.com/article/Object-Masks

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
'''

import SoftLayer.API
import json

USERNAME = 'set me'
API_KEY = 'set me'

brandId = 4

client = SoftLayer.create_client_from_env(username=USERNAME, api_key=API_KEY)

brandService = client['SoftLayer_Brand']
objectMask = "mask[accountStatus[name], masterUser[username], hardwareCount, virtualGuestCount, userCount, openTicketCount]"

try:
    result = brandService.getOwnedAccounts(id=brandId, mask=objectMask)
    print(json.dumps(result, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to list the customers. "
          % (e.faultCode, e.faultString))

```
