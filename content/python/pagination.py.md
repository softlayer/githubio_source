---
title: "pagination.py"
description: "pagination.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
tags:
    - "pagination"
---


```
"""
Example about pagination

The script retrieves the Bare metal servers in a account
and displays all the servers using pagination

Important manual pages
http://sldn.softlayer.com/reference/services/SoftLayer_Account
http://sldn.softlayer.com/reference/services/SoftLayer_Account/getHardware
https://softlayer-api-python-client.readthedocs.org/en/latest/api/client/#module-SoftLayer

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
import SoftLayer

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'

client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)

offset = 0
limit = 1

accountService = client['SoftLayer_Account']

while True:
    try:
        result = accountService.getHardware(limit=limit, offset=offset)
        offset = offset + limit
        limit = limit + limit
        print(result)
        if not result:
            break
    except SoftLayer.SoftLayerAPIError as e:
        print("Unable to retrieve the servers . " % (e.faultCode, e.faultString))
    exit(1)
    
```
