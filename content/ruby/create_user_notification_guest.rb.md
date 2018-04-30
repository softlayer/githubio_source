---
title: "create_user_notification_guest.rb"
description: "create_user_notification_guest.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Product_Package"
    - "SoftLayer_User_Customer_Notification_Virtual_Guest"
tags:
    - "notifications"
---


```
# Add user notification to guest (standard notification)
#
# Important manual pages:
# http://sldn.softlayer.com/reference/services/SoftLayer_User_Customer_Notification_Virtual_Guest
# http://sldn.softlayer.com/reference/services/SoftLayer_User_Customer_Notification_Virtual_Guest/createObjects
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_User_Customer_Notification_Virtual_Guest
#
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc.<sldn@softlayer.com>
require 'softlayer_api'

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY  = 'set me'

template_objects = [
  {
    'complexType' => 'SoftLayer_User_Customer_Notification_Virtual_Guest',
    'guestId' => 490_544_2,
    'userId' => 142_861
  }
]

# Declaring the API client to use the SoftLayer_Product_Package API service
client = SoftLayer::Client.new(username: USERNAME, api_key: API_KEY)
user_notification_service = client.service_named('SoftLayer_User_Customer_Notification_Virtual_Guest')

begin
  # Creating the notification
  result = user_notification_service.createObjects(template_objects)
  puts result
rescue StandardError => exception
  puts "Unable to get templates: #{exception}"
end

```
