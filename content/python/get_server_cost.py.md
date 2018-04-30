---
title: "get_server_cost.py"
description: "get_server_cost.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Hardware_Server"
tags:
    - "billing"
---


```
"""
Get the recurring cost of all servers on your account.

Get a list of servers on a SoftLayer account along with their recurring
monthly costs. We can get that by calling getHardware() in the
SoftLayer_Account API service with an object mask to retrieve cost.

Important manual pages
see http://sldn.softlayer.com/reference/services/SoftLayer_Account/getHardware
see http://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server/getCost

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
import SoftLayer

"""
client configuration
Your SoftLayer API username and key.
"""
USERNAME = 'set me'
API_KEY = 'set me'

# Declare the API client
client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
accountService = client['SoftLayer_Account']

# Add the object mask to the call.
objectMask = "mask(SoftLayer_Hardware_Server).cost"

try:
    # Retrieve our account's hardware records.
    result = accountService.getHardware(mask=objectMask)
    print(result)
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to retrieve the Bare metal list. " % (e.faultCode, e.faultString))
    exit(1)

```
