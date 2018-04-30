---
title: "reset_portal_user_password.py"
description: "reset_portal_user_password.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_User_Customer"
tags:
    - "users"
---


```
"""
Reset portal user password.
This script resets the password of a portal user by SoftLayer_User_Customer::updatePassword method
need to define the new password and pass it to updatePassword() method.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_User_Customer
http://sldn.softlayer.com/reference/services/SoftLayer_User_Customer/updatePassword
@License: http://sldn.softlayer.com/article/License
@Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
# So we can talk to the SoftLayer API:
import SoftLayer
"""
Your SoftLayer API username and key.
Generate an API key at the SoftLayer Customer Portal
"""
API_USERNAME = 'set-me'
API_KEY = 'set-me'

userCustomerId = 152188
newPassword = 'newPassword123!'

# Create a client Object.
client = SoftLayer.Client(username=API_USERNAME, api_key=API_KEY)
try:
    updatePassword = client['SoftLayer_User_Customer'].updatePassword(newPassword, id=userCustomerId)
    print("Password updated!")
except SoftLayer.SoftLayerAPIError as e:
    print("Error cannot update user password  faultCode=%s, faultString=%s"
          % (e.faultCode, e.faultString))
    exit(1)

```
