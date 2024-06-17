---
title: "SuscribeUserUnplainedIncident.rb"
description: "SuscribeUserUnplainedIncident.rb"
date: "2018-04-25"
classes: 
    - "SoftLayer_User_Customer"
tags:
    - "suscribers"
---


```ruby
require 'softlayer_api'
require 'pp'


username = ''
key = 'apikey_goes_here'

#The customer ID you whish add the suscription
customerID = 205830

client = SoftLayer::Client.new( :username => username,:api_key => key)

userClient = client.service_named('SoftLayer_User_Customer')

result = userClient.object_with_id(customerID).addNotificationSubscriber("UNPLANNED_INCIDENT")
# if the notification suscriber has been added we procede to create the suscriberDeliveryMethods
if result
  deliveryMethodKeyNames = [ "EMAIL" ]
  result = userClient.object_with_id(customerID).createSubscriberDeliveryMethods("UNPLANNED_INCIDENT", deliveryMethodKeyNames)
  pp (result)
end


```
