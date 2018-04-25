---
title: "edit_user.py"
description: "edit_user.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_User_Customer"
tags:
    - "users"
---


```
"""
Edit User.
Account master users and sub-users who have the User Manage permission in the SoftLayer customer portal
can update other user's information. Use editObject() if you wish to edit a single user account.
Users who do not have the User Manage permission can only update their own information.
Important manual Pages:
http://sldn.softlayer.com/reference/services/SoftLayer_User_Customer/editObject
http://sldn.softlayer.com/reference/datatypes/SoftLayer_User_Customer
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

# Create a client instance to connect to the API service.
client = SoftLayer.Client(username=API_USERNAME, api_key=API_KEY)

# Set the id of user to edit
userId = 123456

"""
userTemplate contains general information relating to a single SoftLayer customer portal user.
Personal information in this type such as names, addresses,
and phone numbers are not necessarily associated with the customer account the user is assigned to.
"""
userTemplateObject = {
    "address1": "315 Capitol Street",
    "city": "Dallas",
    "companyName": "company name",
    "country": "US",
    "email": "test@softlayer.local",
    "firstName": "myFirstName",
    "lastName": "myLastName",
    "officePhone": 44444,
    "postalCode": 77002,
    "state": "TX",
    "timezoneId": 114,
    "userStatusId": 1001,
    "username": "myUsername"
}
try:
    client['User_Customer'].editObject(userTemplateObject, id=userId)
    print("User Created!")
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to edit user faultCode=%s, faultString=%s"
          % (e.faultCode, e.faultString))
    exit(1)

```
