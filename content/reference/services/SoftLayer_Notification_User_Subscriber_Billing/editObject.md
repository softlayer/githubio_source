---
title: "editObject"
description: "The subscriber's subscription status can be 'turned off' or 'turned on' if the subscription is not required. 

Subscribe... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Notification"
classes:
    - "SoftLayer_Notification_User_Subscriber_Billing"
aliases:
    - "/reference/services/softlayer_notification_user_subscriber_billing/editObject"
---
# [SoftLayer_Notification_User_Subscriber_Billing](/reference/services/SoftLayer_Notification_User_Subscriber_Billing)::editObject


Edit a notification subscriber active status


## Overview 
The subscriber's subscription status can be "turned off" or "turned on" if the subscription is not required. 

Subscriber preferences may also be edited.  To edit the preferences, you must pass in the id off the preferences to edit.  Here is an example of structure to pass in.  In this example, the structure will set the subscriber status to active and the threshold preference to 90 and the limit preference to 20 


*id = 1111
*active = 1
*preferences[1]
**id = 11
**value = 90
*preference[2]
**id = 12
**value = 20

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|templateObject| <a href='/reference/datatypes/SoftLayer_Notification_User_Subscriber_Billing'>SoftLayer_Notification_User_Subscriber_Billing </a>| A skeleton SoftLayer_Notification_User_Subscriber_Billing object with only the properties defined that you wish to change. Unchanged properties are left alone.|


### Required Headers
* authenticate
* SoftLayer_Notification_User_Subscriber_BillingInitParameters


### Return Values
* boolean




