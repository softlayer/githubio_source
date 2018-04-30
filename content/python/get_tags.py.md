---
title: "get_tags.py"
description: "get_tags.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
tags:
    - "metadata"
---


```
"""
Get all the tags in the account.

The script gets all the tags in the account we make a simple
call the the getTags() in the SoftLayer_Account API service.

Important Manual pages
http://sldn.softlayer.com/reference/services/SoftLayer_Account
http://sldn.softlayer.com/reference/services/SoftLayer_Account/getTags

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
import SoftLayer

"""
Client configuration
Your SoftLayer API username and key.
"""
USERNAME = 'set me'
API_KEY = 'set me'

# Declaring the API client
client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
accountService = client['SoftLayer_Account']

try:
    # Getting the tags in the account
    result = accountService.getTags()
    print(result)
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to list the tags faultCode=%s, faultString=%s"
          % (e.faultCode, e.faultString))
    exit(1)

```
