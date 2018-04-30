---
title: "create_user.py"
description: "create_user.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_User_Customer"
tags:
    - "users"
---


```
"""
Create user

The script creates an user, it makes a single call to the
SoftLayer_User_Customer::createObject method.
For more information see below.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_User_Customer/
http://sldn.softlayer.com/reference/services/SoftLayer_User_Customer/createObject
http://sldn.softlayer.com/reference/datatypes/SoftLayer_User_Customer
"""
import SoftLayer

# Your SoftLayer API username.
USERNAME = 'set me'
# Generate one at https://manage.softlayer.com/Administrative/apiKeychain
API_KEY = 'set me'

# Build a skeleton SoftLayer_User_Customer object
# Containing the user you want to create.
templateObject = {
    # Your account ID
    "accountId": 1,
    "address1": "4849 Alpha Rd.",
    "city": "Dallas",
    "companyName": "company name",
    "country": "US",
    "daylightSavingsTimeFlag": True,
    "email": "email@softlayer.com",
    "firstName": "firstName",
    "lastName": "myLastName",
    "officePhone": 442805413,
    # The user ID of the user which is creating this user
    "parentId": 1,
    "postalCode": 72211,
    "state": "TX",
    "timezoneId": 114,
    # 1001 = Active; 1002 = Disable; 1003 = Inactive; 1021 = Delete ; 1022 = VPN Only
    "userStatusId": 1001,
    "username": "userTestRa3"
}

password = "ThePAssword,"
vpnPassword = "ThePAssword,"

# Declare the API client
client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)

try:
    # Getting the metrics
    result = client['SoftLayer_User_Customer'].createObject(templateObject, password, vpnPassword)
    print(result)
except SoftLayer.SoftLayerAPIError as e:
    # If there was an error returned from the SoftLayer API then bomb out with the
    # Error message.
    print("Unable to create the user faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))

```
