---
title: "set_api_ip_address_restriction.py"
description: "set_api_ip_address_restriction.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_User_Customer"
    - "SoftLayer_Account"
    - "SoftLayer_User_Customer_ApiAuthentication"
tags:
    - "users"
---


```
"""
Set API IP address restriction.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Account/getUsers
http://sldn.softlayer.com/reference/services/SoftLayer_User_Customer/getApiAuthenticationKeys
http://sldn.softlayer.com/reference/services/SoftLayer_User_Customer_ApiAuthentication/editObject
http://sldn.softlayer.com/reference/datypes/SoftLayer_User_Customer_ApiAuthentication/editObject
http://sldn.softlayer.com/article/Object-Filters

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer
import json

USERNAME = 'set me'
API_KEY = 'set me'

userName = "set me"

ip = "10.10.10.10"

client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
accountService = client['SoftLayer_Account']
userService = client['SoftLayer_User_Customer']
keyService = client['SoftLayer_User_Customer_ApiAuthentication']

objectFilterUser = {"users": {"username": {"operation": userName}}}

try:
    users = accountService.getUsers(filter=objectFilterUser)
    keys = userService.getApiAuthenticationKeys(id=users[0]['id'])
    keys[0]["ipAddressRestriction"] = ip
    result = keyService.editObject(keys[0], id=keys[0]['id'])
    print(json.dumps(result, sort_keys=True, indent=2, separators=(',', ': ')))

except SoftLayer.SoftLayerAPIError as e:
    print("Unable to set API IP address restriction. faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))

```
