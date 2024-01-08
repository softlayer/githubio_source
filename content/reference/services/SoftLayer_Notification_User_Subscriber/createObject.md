---
title: "createObject"
description: "Use the method to create a new subscription for a notification.  This method is the entry method to the notification system. Certain properties are required to create a subscription while others are optional. 

The required property is the resourceRecord property which is type SoftLayer_Notification_User_Subscriber_Resource.  For the resourceRecord property, the only property that needs to be populated is the resourceTableId.  The resourceTableId is the unique identifier of a SoftLayer service to create the subscription for.  For example, the unique identifier of the Storage Evault service to create the subscription on. 

Optional properties that can be set is the preferences property.  The preference property is an array SoftLayer_Notification_User_Subscriber_Preference. By default, the system will populate the preferences with the default values if no preferences are passed in.  The preferences passed in must be the preferences related to the notification subscribing to.  The notification preferences and preference details (such as minimum and maximum values) can be retrieved using the SoftLayer_Notification service.  The properties that need to be populated for preferences are the notificationPreferenceId and value. 

For example to create a subscriber for a Storage EVault service to be notified 15 times during a billing cycle and to be notified when the vault usage reaches 85% of its allowed capacity use the following structure: 


*userRecordId = 1111
*notificationId = 3
*resourceRecord
**resourceTableId = 1234
*preferences[1]
**notificationPreferenceId = 2
**value = 85
*preference[2]
**notificationPreferenceId = 3
**value = 15

"
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Notification"
classes:
    - "SoftLayer_Notification_User_Subscriber"
type: "reference"
layout: "method"
mainService : "SoftLayer_Notification_User_Subscriber"
---

### [REST Example](#createObject-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#createObject-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Notification_User_Subscriber]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Notification_User_Subscriber/createObject'
```
