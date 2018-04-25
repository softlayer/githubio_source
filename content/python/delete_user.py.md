---
title: "delete_user.py"
description: "delete_user.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_User_Customer"
    - "SoftLayer_Account"
tags:
    - "users"
---


```
"""
Delete user.
This scripts allows to delete a given user, it retrieves the SoftLayer_User_Customer object
by the SoftLayer_User_Customer::getObject method and changes the status of user to deleted.
Important manual pages:
http://sldn.softlayer.com/reference/datatypes/SoftLayer_User_Customer
http://sldn.softlayer.com/reference/services/SoftLayer_User_Customer/editObject
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

# Set the user ID of the user you want to delete, you can get them using
# The method SoftLayer_Account::getUsers.
userId = 162123
# Create a client object.
client = SoftLayer.Client(username=API_USERNAME, api_key=API_KEY)
try:
    userToDelete = client['User_Customer'].getObject(id=userId)
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to get user information, faultCode=%s, faultString=%s"
          % (e.faultCode, e.faultString))
    exit(1)
# Set the user status to delete, these are the possible status for user
# 1001 = Active; 1002 = Disable; 1003 = Inactive; 1021 = Delete ; 1022 = VPN Only
userToDelete['userStatusId'] = 1021
try:
    userDeleted = client['User_Customer'].editObject(userToDelete, id=userId)
    print("User deleted!")
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to delete user, faultCode=%s, faultString=%s"
          % (e.faultCode, e.faultString))
    exit(1)

```
