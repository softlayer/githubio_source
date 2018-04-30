---
title: "add_user_permissions.py"
description: "add_user_permissions.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_User_Customer"
    - "SoftLayer_Account"
    - "SoftLayer_User_Customer_CustomerPermission_Permission"
tags:
    - "users"
---


```
"""
Add user permission.
This script adds a single permission to an user.
Use the SoftLayer_User_Customer_CustomerPermission_Permission::getAllObjects method
to retrieve a list of all permissions available in the SoftLayer.
Important manual Pages:
http://sldn.softlayer.com/reference/services/SoftLayer_User_Customer/addPortalPermission
http://sldn.softlayer.com/reference/datatypes/SoftLayer_User_Customer_CustomerPermission_Permission
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
"""
Set the user ID of the user you want to add permissions, you can get it using
the method SoftLayer_Account::getUsers.
"""
userId = 111922
# Create a client object to connect to API services.
client = SoftLayer.Client(username=API_USERNAME, api_key=API_KEY)
"""
In this example we are going to add permissions to the user
to add tickets using SoftLayer_User_Customer::addPortalPermission method, use the
SoftLayer_User_Customer_CustomerPermission_Permission::getAllObjects method to get a list of permissions to put
the values into a SoftLayer_User_Customer_CustomerPermission_Permission object and pass to addPortalPermission() method
"""
permissionsTemplate = {
    'keyName': 'TICKET_ADD'
}
try:
    client['SoftLayer_User_Customer'].addPortalPermission(permissionsTemplate, id=userId)
    print("User permission updated!")
except SoftLayer.SoftLayerAPIError as e:
    print("Error to add permission to user faultCode=%s, faultString=%s"
          % (e.faultCode, e.faultString))
    exit(1)

```
