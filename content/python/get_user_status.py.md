---
title: "get_user_status.py"
description: "get_user_status.py"
date: "2018-04-25"
classes: 
    - "SoftLayer_User_Customer"
    - "SoftLayer_Account"
tags:
    - "users"
---


```
"""
Get User status.
This script will list the status of sub-users similar to the view displayed at
https://control.softlayer.com/account/users
it calls to SoftLayer_User_Customer::getChildUsers
method to retrieve the user list.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Account/getUsers
http://sldn.softlayer.com/reference/datatypes/SoftLayer_User_Customer
@License: http://sldn.softlayer.com/article/License
@Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

# So we can talk to the SoftLayer API:
import SoftLayer
from prettytable import PrettyTable

"""
 Your SoftLayer API username and key.
 Generate an API key at the SoftLayer Customer Portal
"""
API_USERNAME = ''
API_KEY = 'apikey_goes_here'

# Set the User ID of the user we want to get the information, we can get this information by
# SoftLayer_Account::getUsers method.
userId = 205824

# Create a client object.
client = SoftLayer.Client(username=API_USERNAME, api_key=API_KEY)

try:
    users = client['User_Customer'].getChildUsers(id=userId)
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to get users information, faultCode=%s, faultString=%s"
          % (e.faultCode, e.faultString))
    exit(1)
table = []
for user in users:
    table.append(
        [user['lastName'], user['firstName'], user['username'], user['userStatusId'], user['sslVpnAllowedFlag']])
userStatus = PrettyTable(["Last Name", "First Name", "User Name", "Status", "VPN Access"])
userStatus.align["ID"] = "l"
userStatus.padding_width = 1
for row in table:
    userStatus.add_row([row[0], row[1], row[2], row[3], row[4]])
print(userStatus)

```
