---
title: "add_portal_permission.py"
description: "add_portal_permission.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_User_Customer"
    - "SoftLayer_User_Customer_CustomerPermission_Permission"
tags:
    - "permissions"
---


```
"""
Add permissions to user

The script adds permissions to an arbitrary user by making a
single call to the SoftLayer_User_Customer::addBulkPortalPermission method.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_User_Customer/
http://sldn.softlayer.com/reference/services/SoftLayer_User_Customer/addBulkPortalPermission
http://sldn.softlayer.com/reference/datatypes/SoftLayer_User_Customer_CustomerPermission_Permission

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
import SoftLayer

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'

# The user id you wish to add permissions
userId = 213758

"""
You can get all permissions by calling the SoftLayer_User_Customer_CustomerPermission_Permission::getAllObjects method
see http://sldn.softlayer.com/reference/services/SoftLayer_User_Customer_CustomerPermission_Permission/getAllObjects for more information
example you can make the Following RESTFul call to get the available permissions
URL: https://<your-username>:<your-key>@api.softlayer.com/rest/v3/SoftLayer_User_Customer_CustomerPermission_Permission/getAllObjects.json?
Method: GET
"""
permissions = [
    {
        "keyName": "TICKET_VIEW",
        "name": "View Tickets",
        'complexType': 'SoftLayer_User_Customer_CustomerPermission_Permission'
    },

    {
        "keyName": "ACCOUNT_SUMMARY_VIEW",
        "name": "view account summary",
        'complexType': 'SoftLayer_User_Customer_CustomerPermission_Permission'
    },
    {
        "keyName": "TICKET_SEARCH",
        "name": "Search Tickets",
        'complexType': 'SoftLayer_User_Customer_CustomerPermission_Permission'
    },
    {
        "keyName": "TICKET_ADD",
        "name": "Add Tickets",
        'complexType': 'SoftLayer_User_Customer_CustomerPermission_Permission'
    },
    {
        "keyName": "TICKET_VIEW_BY_HARDWARE",
        "name": "View Tickets by Hardware Access",
        'complexType': 'SoftLayer_User_Customer_CustomerPermission_Permission'
    },
    {
        "keyName": "TICKET_VIEW_BY_VIRTUAL_GUEST",
        "name": "View Tickets by Computing Instance Access",
        'complexType': 'SoftLayer_User_Customer_CustomerPermission_Permission'
    }
]

# Declare the API client
client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
userCustomerService = client['SoftLayer_User_Customer']

try:
    # Adding portal permissions
    result = userCustomerService.addBulkPortalPermission(permissions, id=userId)
    print(result)
except SoftLayer.SoftLayerAPIError as e:
    """
    If there was an error returned from the SoftLayer API then bomb out with the
    error message.
    """
    print("Unable to add permissions. "
          % (e.faultCode, e.faultString))

```
