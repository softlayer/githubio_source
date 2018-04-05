---
title: "Events"
description: "Going over Events with some examples of what each might look like"
date: "2018-04-05"
classes:
    - "SoftLayer_Notification_Occurrence_Event"
tags:
    - "resultlimit"
    - "objectmask"
    - "objectfilter"
    - "event"
---

# Events
[SoftLayer_Notification_Occurrence_Events](https://softlayer.github.io/reference/services/SoftLayer_Notification_Occurrence_Event/) at SoftLayer are how we communicate maintenance, outages, and other disruptive events to customers. In the control portal, you can find these at https://control.softlayer.com/event/announcement

## Get All Events

[SoftLayer_Notification_Occurrence_Event::getAllObjects()](https://softlayer.github.io/reference/services/SoftLayer_Notification_Occurrence_Event/getAllObjects/)
```
curl -u $SL_USER:$SL_APIKEY 'https://api.softlayer.com/rest/v3.1/SoftLayer_Notification_Occurrence_Event/getAllObjects.json
```

The output will look something like this, but will have every event that has ever been reported on your account. For brevity I have only included 1 Event
```
[
    {
        "endDate": null,
        "id": 2584,
        "lastImpactedUserCount": 11232,
        "modifyDate": "2016-06-13T08:27:20-06:00",
        "recoveryTime": null,
        "startDate": "2014-03-31T00:35:00-06:00",
        "statusCode": {
            "keyName": "COMPLETED",
            "name": "Completed"
        },
        "subject": "IPv6 Sessions Down on FCR02.DAL05",
        "summary": "At 31-Mar-2014 06:35 UTC the Network Operations Center was alerted that the IPv6 BGP session on frontend customer router (FCR) fcr02.dal05 had dropped.  Network Engineers began investigating the issue and found a customer was sending a high rate of IPv6 packets destined to fcr02.dal05.  Network Engineers mitigated the issue at 31-Mar-2014 07:16 UTC.",
        "systemTicketId": 9266184
    }
]
```

## Get Open Events
To find all the open events, look for statusCode = ACTIVE

https://api.softlayer.com/rest/v3.1/SoftLayer_Notification_Occurrence_Event/getAllObjects.json?
objectMask=mask[notificationOccurrenceEventType]
resultLimit=0,10
objectFilter={"statusCode":+{"keyName":+{"operation":+"ACTIVE"}}}'

```
curl -u $SL_USER:$SL_APIKEY -X GET -H "Accept: */*" -H "Accept-Encoding: gzip, deflate, compress"  'https://api.softlayer.com/rest/v3.1/SoftLayer_Notification_Occurrence_Event/getAllObjects.json?objectMask=mask%5BnotificationOccurrenceEventType%5D&resultLimit=0%2C10&objectFilter=%7B%22statusCode%22%3A+%7B%22keyName%22%3A+%7B%22operation%22%3A+%22ACTIVE%22%7D%7D%7D'
```

```
{'endDate': '2018-04-05T17:00:00-06:00',
  'id': 116425,
  'lastImpactedUserCount': 581,
  'modifyDate': '2018-04-05T07:35:20-06:00',
  'notificationOccurrenceEventType': {'keyName': 'PLANNED'},
  'recoveryTime': None,
  'startDate': '2018-04-05T04:00:00-06:00',
  'statusCode': {'keyName': 'ACTIVE', 'name': 'Active'},
  'subject': 'Scheduled Maintenance: WDC04 Critical Power Maintenance',
  'summary': 'Dear IBM Customer, \r\n'
             '\r\n'
             'IBM Cloud in coordination with our vendors will be performing a '
             'Critical Power Maintenance at WDC04 starting on Thursday, April '
             '5th, 2018.  The window for this maintenance is 06:00am EST to '
             '19:00pm EST.\r\n'
             '\r\n'
             'We Do not expect any major impact to our servers or services '
             'during this maintenance.  The only expected impact during this '
             'maintenance will be a loss of redundancy at the server level '
             'only for a short period of time as they work on the Secondary '
             'power source and a 5-10 minute loss of IPMI functionality during '
             'the transition to alternative power source at the start and end '
             'of the maintenace but will not be an extended period of time.\r\n'
             '\r\n'
             'If additional preventative course of action is required to '
             'minimize service impact, further notification(s) will be '
             'provided. In the event of an unexpected impact, we will work '
             'with our Data Center Staff and on-site Engineers to take '
             'immediate action to bring critical services back on-line as '
             'quickly as possible. \r\n'
             '\r\n'
             '\r\n'
             '***Scheduled Date(s): Thursday, April 5th, 2018 \r\n'
             '***Scheduled Time(s): 06:00am EST to 19:00pm EST Please contact '
             'our support department should you have any questions or '
             'concerns.',
  'systemTicketId': 58076149},
```

## Get Recent Events


# Event Types

# EFfected Machines