---
title: "delete_notification_subscriber.py"
description: "delete_notification_subscriber.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_User_Customer_Notification_Virtual_Guest"
tags:
    - "monitoring"
---


```
"""
Delete a notification subscription

The script deletes a notification for a determinate user in a determinate Virtual Guest
for more reference see these reference pages

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_User_Customer_Notification_Virtual_Guest/deleteObjects
http://sldn.softlayer.com/reference/datatypes/SoftLayer_User_Customer_Notification_Virtual_Guest

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
which contains the id we wish to delete
To get the notifications for an determinate Virtual Guest
call the getObject method + the mask "mask[monitoringUserNotification]"
e.g.
guestId = 7698972
guest = client['Virtual_Guest'].getObject(id=guestId, mask="mask[monitoringUserNotification]")
notifications = guest['monitoringUserNotification']
print (notifications)
"""
notification = [
    {
        'id': 2154178
    }
]

try:
    result = userCustomerNotification.deleteObjects(notification)
    pp(result)
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to delete the notification "
          % (e.faultCode, e.faultString))
    exit(1)

```
