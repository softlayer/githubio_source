---
title: "create_notification_subscribers.py"
description: "create_notification_subscribers.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_User_Customer_Notification_Virtual_Guests"
    - "SoftLayer_User_Customer_Notification_Virtual_Guest"
tags:
    - "monitoring"
---


```
"""
Create a notification subscription

The script creates a notification for a determinate user in a determinate Virtual Guest
for more reference see these reference pages

Important manual pages
http://sldn.softlayer.com/reference/services/SoftLayer_User_Customer_Notification_Virtual_Guest/createObject
http://sldn.softlayer.com/reference/datatypes/SoftLayer_User_Customer_Notification_Virtual_Guests

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
import SoftLayer.API
from pprint import pprint as pp

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'

# Declare the API client
client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
userCustomerNotification = client['SoftLayer_User_Customer_Notification_Virtual_Guest']

"""
Build a SoftLayer_User_Customer_Notification_Virtual_Guest skeleton object
which contains the virtual guest id and user id of the notification
"""
newNotification = [
    {
        'guestId': 7698972,
        'userId': 205832
    }
]

try:
    result = userCustomerNotification.createObjects(newNotification)
    pp(result)
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to create the notification "
          % (e.faultCode, e.faultString))
    exit(1)

```
