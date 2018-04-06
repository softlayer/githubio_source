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

statusCode = COMPLETED is also an option.

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


# Event Types

Events can be PLANNED, UNPLANNED_INCIDENT, or ANNOUNCEMENT. 

## PLANNED
Planned events are usually announced a few weeks in advanced, and cover things like router upgrades, VSI reboots, and other work that needs to be done to improve our products.

This will get all the PLANNED and ACTIVE events going on.
https://api.softlayer.com/rest/v3.1/SoftLayer_Notification_Occurrence_Event/getAllObjects.json?
objectMask=mask[notificationOccurrenceEventType]&
objectFilter={
    "notificationOccurrenceEventType":{"keyName":{"operation":+"PLANNED"}},
    "statusCode":{"keyName":{"operation":"ACTIVE"}}}'

```
curl -u $SL_USER:$SL_APIKEY -X GET -H "Accept: */*" -H "Accept-Encoding: gzip, deflate, compress"  'https://api.softlayer.com/rest/v3.1/SoftLayer_Notification_Occurrence_Event/getAllObjects.json?objectMask=mask%5BnotificationOccurrenceEventType%5D&objectFilter=%7B%22notificationOccurrenceEventType%22%3A+%7B%22keyName%22%3A+%7B%22operation%22%3A+%22PLANNED%22%7D%7D%2C+%22statusCode%22%3A+%7B%22keyName%22%3A+%7B%22operation%22%3A+%22ACTIVE%22%7D%7D%7D'
```

Output:
```
 {'endDate': '2017-08-19T19:00:00-06:00',
  'id': 81507,
  'lastImpactedUserCount': 284685,
  'modifyDate': '2017-08-19T13:25:50-06:00',
  'notificationOccurrenceEventType': {'keyName': 'PLANNED'},
  'recoveryTime': None,
  'startDate': '2017-08-19T13:00:00-06:00',
  'statusCode': {'keyName': 'ACTIVE', 'name': 'Active'},
  'subject': 'Emergency Planned IMS Maintenance',
  'summary': 'The IBM Cloud system engineers will be performing an emergency '
             'IMS application database system maintenance. During this '
             'maintenance we do not expect any IMS database or application '
             'system downtime. The purpose of the maintenance is to resolve '
             'IMS database system issues. When the maintenance tasks are '
             'completed, notifications will be sent out stating that IMS '
             'application database maintenance has been successfully '
             'completed.\r\n',
  'systemTicketId': 44279325}
```

## UNPLANNED_INCIDENT 
Unplanned incidents are a whole variety of things that might impact services.


This query will get all the UNPLANNED_INCIDENTS that were created AFTER  04/01/2018 01:00:00. https://softlayer.github.io/article/object-filters/ has more details on other date time operations you can use.

https://api.softlayer.com/rest/v3.1/SoftLayer_Notification_Occurrence_Event/getAllObjects.json?
objectMask=mask[id,+startDate,+notificationOccurrenceEventType]&
objectFilter={
    "notificationOccurrenceEventType":
        {"keyName":{"operation":"UNPLANNED_INCIDENT"}
    }
    "startDate":
        {"operation":"greaterThanDate",
         "options":[{"name":"date","value":["04/01/2018 01:00:00"]}]
    }
}

```
curl -u $SL_USER:$SL_APIKEY -X GET -H "Accept: */*" -H "Accept-Encoding: gzip, deflate, compress"  'https://api.softlayer.com/rest/v3.1/SoftLayer_Notification_Occurrence_Event/getAllObjects.json?objectMask=mask%5Bid%2C+startDate%2C+notificationOccurrenceEventType%5D&objectFilter=%7B%22notificationOccurrenceEventType%22%3A+%7B%22keyName%22%3A+%7B%22operation%22%3A+%22UNPLANNED_INCIDENT%22%7D%7D%2C+%22startDate%22%3A+%7B%22operation%22%3A+%22greaterThanDate%22%2C+%22options%22%3A+%5B%7B%22name%22%3A+%22date%22%2C+%22value%22%3A+%5B%2204%2F01%2F2018+01%3A00%3A00%22%5D%7D%5D%7D%7D'
```

Output
```
{'endDate': '2018-04-02T23:41:00-06:00',
  'id': 116225,
  'lastImpactedUserCount': 7905,
  'modifyDate': '2018-04-03T11:04:32-06:00',
  'notificationOccurrenceEventType': {'keyName': 'UNPLANNED_INCIDENT'},
  'recoveryTime': None,
  'startDate': '2018-04-02T23:34:00-06:00',
  'statusCode': {'keyName': 'ACTIVE', 'name': 'Active'},
  'subject': 'Private network degradation in DCs in Dallas region',
  'summary': 'At 03-Apr-2018 5:03 UTC the Network Operation Center was alerted '
             'to communication failures for the backend private networks in '
             'the Dallas Region. Network Engineers are investigating at this '
             'time. We will provide more detail as it becomes available.',
  'systemTicketId': 58021829}
```


## ANNOUNCEMENT 
Announcements are the 'everything else' category. Not usually disruptive, will usually be things like end of life announcements.

This time I've changed the objectMask to include the lastUpdate and restrict other local fields to limit the amount of information we get back to fields I care about at the moment.


https://api.softlayer.com/rest/v3.1/SoftLayer_Notification_Occurrence_Event/getAllObjects.json?
objectMask=mask[
    id, startDate, subject, lastUpdate ,notificationOccurrenceEventType
]&
objectFilter=
    {"notificationOccurrenceEventType":
        {"keyName":{"operation":"ANNOUNCEMENT"}}
    }'


```
curl -u $SL_USER:$SL_APIKEY -X GET -H "Accept: */*" -H "Accept-Encoding: gzip, deflate, compress"  'https://api.softlayer.com/rest/v3.1/SoftLayer_Notification_Occurrence_Event/getAllObjects.json?objectMask=mask%5Bid%2CstartDate%2Csubject%2ClastUpdate%2CnotificationOccurrenceEventType%5D&objectFilter=%7B%22notificationOccurrenceEventType%22%3A+%7B%22keyName%22%3A+%7B%22operation%22%3A+%22ANNOUNCEMENT%22%7D%7D%7D'
```

Output:
```
  'id': 106105,
  'lastUpdate': {'contents': 'IBM Cloud engineers have received patches from '
                             'Red Hat that address the Meltdown and Spectre '
                             'security vulnerabilities.\r\n'
                             '\r\n'
                             'New image only available for Red Hat Enterprise '
                             'Linux 7.x at this time. \r\n'
                             '\r\n'
                             'As always - before applying new images, IBM '
                             'Cloud recommends testing to ensure a smooth '
                             'transition for your environment.\r\n'
                             '\r\n'
                             '\r\n'
                             'IBM Cloud',
                 'createDate': '2018-01-17T13:44:51-06:00',
                 'endDate': None,
                 'startDate': '2018-01-17T13:44:51-06:00'},
  'notificationOccurrenceEventType': {'keyName': 'ANNOUNCEMENT'},
  'startDate': None,
  'subject': 'New Red Hat Enterprise Linux 7 Images Available'
```


# Event Specifics
Now that we know how to deal with getting a list of all events, lets dive into a specific event.

The most recent Active event I have is going to be this one.

```
  'endDate': '2018-04-02T23:41:00-06:00',
  'id': 116225,
  'lastImpactedUserCount': 7905,
  'modifyDate': '2018-04-03T11:04:32-06:00',
  'notificationOccurrenceEventType': {'keyName': 'UNPLANNED_INCIDENT'},
  'recoveryTime': None,
  'startDate': '2018-04-02T23:34:00-06:00',
  'statusCode': {'keyName': 'ACTIVE', 'name': 'Active'},
  'subject': 'Private network degradation in DCs in Dallas region',
```

## Effected Machines
To see what machines on our account are effected by this event, we need to tap into the [impactedResources](https://softlayer.github.io/reference/datatypes/SoftLayer_Notification_Occurrence_Resource/) relational property. There is also impactedAccounts and impactedUsers that work the same way. 


```
curl -u $SL_USER:$SL_APIKEY -X GET -H "Accept: */*" -H "Accept-Encoding: gzip, deflate, compress"  'https://api.softlayer.com/rest/v3.1/SoftLayer_Notification_Occurrence_Event/116225/getObject.json?objectMask=mask%5Bid%2CstartDate%2Csubject%2CimpactedResources%5D'
```

Output:
```
{'id': 116225,
 'impactedResources': [{'active': 1,
                        'filterLabel': 'dal01',
                        'hostname': 'testvpn.test.com',
                        'notificationOccurrenceEventId': 116225,
                        'privateIp': '10.17.223.157',
                        'publicIp': '208.43.49.207',
                        'resourceAccountId': 307608,
                        'resourceName': 'testvpn.test.com',
                        'resourceTableId': 218467,
                        'resourceType': 'SERVER'},
                       {'active': 1,
                        'filterLabel': 'dal01',
                        'hostname': 'domain-master.lablayer.info',
                        'notificationOccurrenceEventId': 116225,
                        'privateIp': '10.37.82.159',
                        'publicIp': '173.193.23.40',
                        'resourceAccountId': 307608,
                        'resourceName': 'domain-master.lablayer.info',
                        'resourceTableId': 662657,
                        'resourceType': 'SERVER'}],
 'startDate': '2018-04-02T23:34:00-06:00',
 'subject': 'Private network degradation in DCs in Dallas region'}
```

If the resource is a storage volume, the output would look more like this
```
{'id': 115025,
 'impactedResources': [{'active': 1,
                        'filterLabel': 'Storage Type 02 File Cluster '
                                       'stff-syd0101',
                        'hostname': 'SL02SV307608_1',
                        'notificationOccurrenceEventId': 115025,
                        'privateIp': 'fsf-syd0101a-fz.service.softlayer.com',
                        'resourceAccountId': 307608,
                        'resourceName': 'SL02SV307608_1',
                        'resourceTableId': 39134586,
                        'resourceType': 'STORAGE_NAS'}],
 'startDate': '2018-04-02T05:20:00-06:00',
 'subject': 'PLANNED MAINTENANCE: Performance/Endurance File Storage Services '
            'in SYD01'}
```


## Updates
Over the course of an event, SoftLayer employees working to resolve the event will update it with progress if needed. To get that information, tap into the [updates](https://softlayer.github.io/reference/datatypes/SoftLayer_Notification_Occurrence_Update) relational property

```
curl -u $SL_USER:$SL_APIKEY -X GET -H "Accept: */*" -H "Accept-Encoding: gzip, deflate, compress"  'https://api.softlayer.com/rest/v3.1/SoftLayer_Notification_Occurrence_Event/116225/getObject.json?objectMask=mask%5Bid%2CstartDate%2Csubject%2Cupdates%5D'
```

Output: 

```
{'id': 116225,
 'startDate': '2018-04-02T23:34:00-06:00',
 'subject': 'Private network degradation in DCs in Dallas region',
 'updates': [{'contents': 'At 06:48 UTC network engineers performed a '
                          'supervisor failover on mbr01.dal01 which restored '
                          'backend connectivity for affected hosts. A reboot '
                          'and disk check may be required for virtual hosts '
                          "which use SAN. If you're still experiencing issues "
                          'please contact support via phone, chat or ticket '
                          'and reference event ID #58021829.',
              'createDate': '2018-04-03T01:45:20-06:00',
              'endDate': None,
              'startDate': '2018-04-03T01:44:00-06:00'},
             {'contents': 'As of 03-April-2018 06:45 UTC network engineers are '
                          'still investigating and working to restore '
                          'connectivity as soon as possible.',
              'createDate': '2018-04-03T00:50:08-06:00',
              'endDate': None,
              'startDate': '2018-04-03T00:49:00-06:00'},
             {'contents': 'At 03-Apr-2018 5:03 UTC the Network Operation '
                          'Center was alerted to communication failures for '
                          'the backend private networks in the Dallas Region. '
                          'Network Engineers are investigating at this time. '
                          'We will provide more detail as it becomes '
                          'available.',
              'createDate': '2018-04-02T23:36:57-06:00',
              'endDate': None,
              'startDate': '2018-04-02T23:36:57-06:00'}]}
```


## Ack Events
To Acknowledge events (this just makes them not pop-up in the control portal) use the [acknowledgeNotification method](https://softlayer.github.io/reference/services/SoftLayer_Notification_Occurrence_Event/acknowledgeNotification/)

Use the [acknowledgeFlag](https://softlayer.github.io/reference/datatypes/SoftLayer_Notification_Occurrence_Event/#acknowledgedFlag) to determine if an incident is in an acknowledged state or not.

List all unacknowledged events
```
curl -u $SL_USER:$SL_APIKEY -X GET -H "Accept: */*" -H "Accept-Encoding: gzip, deflate, compress"  'https://api.softlayer.com/rest/v3.1/SoftLayer_Notification_Occurrence_Event/getAllObjects.json?objectMask=mask%5Bid%2CstartDate%2Csubject%2CnotificationOccurrenceEventType%2CacknowledgedFlag%5D&objectFilter=%7B%22acknowledgedFlag%22%3A+%7B%22operation%22%3A+0%7D%7D'
```



Get the event, notice its unacknowledged
```
curl -u $SL_USER:$SL_APIKEY -X GET -H "Accept: */*" -H "Accept-Encoding: gzip, deflate, compress"  'https://api.softlayer.com/rest/v3.1/SoftLayer_Notification_Occurrence_Event/116225/getObject.json?objectMask=mask%5Bid%2CstartDate%2Csubject%2CnotificationOccurrenceEventType%2CacknowledgedFlag%5D'
```

Acknowledge an event

```
curl -u $SL_USER:$SL_APIKEY -X GET -H "Accept: */*" -H "Accept-Encoding: gzip, deflate, compress"  'https://api.softlayer.com/rest/v3.1/SoftLayer_Notification_Occurrence_Event/116225/acknowledgeNotification.json'
```

Get the event, notice its acknowledged
```
curl -u $SL_USER:$SL_APIKEY -X GET -H "Accept: */*" -H "Accept-Encoding: gzip, deflate, compress"  'https://api.softlayer.com/rest/v3.1/SoftLayer_Notification_Occurrence_Event/116225/getObject.json?objectMask=mask%5Bid%2CstartDate%2Csubject%2CnotificationOccurrenceEventType%2CacknowledgedFlag%5D'
```

Output:
```
{'acknowledgedFlag': False,
 'id': 116225,
 'notificationOccurrenceEventType': {'keyName': 'UNPLANNED_INCIDENT'},
 'startDate': '2018-04-02T23:34:00-06:00',
 'subject': 'Private network degradation in DCs in Dallas region'}
True
{'acknowledgedFlag': True,
 'id': 116225,
 'notificationOccurrenceEventType': {'keyName': 'UNPLANNED_INCIDENT'},
 'startDate': '2018-04-02T23:34:00-06:00',
 'subject': 'Private network degradation in DCs in Dallas region'}
```
