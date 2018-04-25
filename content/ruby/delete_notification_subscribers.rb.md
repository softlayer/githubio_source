---
title: "delete_notification_subscribers.rb"
description: "delete_notification_subscribers.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_User_Customer_Notification_Virtual_Guest"
tags:
    - "monitoring"
---


```
# Delete a notification subscription
#
# The script deletes a notification for a determinate user in a determinate Virtual Guest
# for more reference see these reference pages
#
# Important manual pages:
# http://sldn.softlayer.com/reference/services/SoftLayer_User_Customer_Notification_Virtual_Guest/deleteObjects
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_User_Customer_Notification_Virtual_Guest
#
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
require 'softlayer_api'
require 'pp'

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'

# Build a SoftLayer_User_Customer_Notification_Virtual_Guest skeleton object
# which contains the id we wish to delete
# To get the notifications for an particular Virtual Guest
# call the getObject method + the mask "mask[monitoringUserNotification]"
# e.g.
# guest_id = 7698972
# guest = client.service_named('Virtual_Guest').object_with_id(guest_id).object_mask("mask[monitoringUserNotification]").getObject()
# notifications = guest['monitoringUserNotification']
# print (notifications)
notification = [
  {
    'id' => 2_147_546
  }
]

# Declare the API client
client = SoftLayer::Client.new(username: USERNAME, api_key: API_KEY)
user_customer_notificiation = client.service_named('SoftLayer_User_Customer_Notification_Virtual_Guest')

begin
  result = user_customer_notificiation.deleteObjects(notification)
  print(result)
rescue StandardError => e
  puts "Unable to delete the notification :-( -- #{e}"
end

```
