---
title: "create_portal_user.py"
description: "create_portal_user.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_User_Customer"
tags:
    - "users"
---


```
"""
Create Portal User.
This script will create a new portal user based in the values set into a SoftLayer_User_Customer
template object and then it will pass to SoftLayer_User_Customer::createObject method.
Check below references for more details.
Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_User_Customer/createObject
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

# Set the password for the new user
userPassword = "Password!123"

# Set the vpn password for the new user
vpnPassword = "Password!123"
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
    result = client['User_Customer'].createObject(userTemplateObject, userPassword, vpnPassword)
    print("User Created!")
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to create new user faultCode=%s, faultString=%s"
          % (e.faultCode, e.faultString))
    exit(1)

```
