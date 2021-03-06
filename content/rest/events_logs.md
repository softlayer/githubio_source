---
title: "Working with Event Logs"
description: "Going over Event Logs with some examples of what each might look like"
date: "2021-03-30"
classes:
    - "SoftLayer_Event_Log"
tags:
    - "eventlogs"
    - "resultlimit"
    - "objectmask"
    - "objectfilter"
---

# Event Log
This example deals with a few ways of pulling data from [SoftLayer_Event_Log](https://sldn.softlayer.com/reference/services/SoftLayer_Event_Log/). There can be quite a few Logs here, so using a filter it recommends like in the [Get Recent Events](#get-recent-events) to limit how far back your search for Events, otherwise you will be paging through Events for a long time.

## [Get All Events](#get-all-events) {#get-all-events .anchor-link}

To get all Events logs, We use [SoftLayer_Event_Log::getAllObjects()](https://softlayer.github.io/reference/services/SoftLayer_Event_Log/getAllObjects/), in this case just the first 50 events by using pagination as `resultLimit=0,50`,  See [Using Result Limits in the SoftLayer API](https://sldn.softlayer.com/article/using-result-limits-softlayer-api/). Also, We add a mask `mask[eventName,eventCreateDate,userType]` to restrict other local fields to limit the amount of information We get back to fields We care about at the moment.

```bash
https://api.softlayer.com/rest/v3.1/SoftLayer_Event_Log/getAllObjects.json?
                    resultLimit=0,50&
                    objectMask=mask[eventName,eventCreateDate,userType]
```
```bash
curl -g -u $SL_USER:$SL_APIKEY 'https://api.softlayer.com/rest/v3.1/SoftLayer_Event_Log/getAllObjects.json?objectMask=mask[eventName,eventCreateDate,userType]&resultLimit=0,50'
```

The output will look something like this,in this case just the first event in the list.
```json
[
    {
        "eventCreateDate": "2021-03-29T14:41:55.444089-06:00",
        "eventName": "Login Successful",
        "userType": "CUSTOMER"
    }
  ]

```

## [Get Recent Events](#get-recent-events) {#get-recent-events .anchor-link}

This query will get all the Recent Events that were created AFTER `03/29/2021 01:00:00` (this date is just an example so keep in mind updating the date example to retrieve the most recent events), [object-filters](https://sldn.softlayer.com/article/object-filters/) has more details on other date time operations you can use.

```bash
https://api.softlayer.com/rest/v3.1/SoftLayer_Event_Log/getAllObjects.json?
            resultLimit=0,50&
            objectMask=mask[eventName,eventCreateDate,userType]&
            objectFilter={"eventCreateDate":{"operation":"greaterThanDate","options":[{"name":"date","value":["2021-03-29T00:00:00.0000-06:00"]}]}}
     
```

```bash
curl -g -u $SL_USER:$SL_APIKEY 'https://api.softlayer.com/rest/v3.1/SoftLayer_Event_Log/getAllObjects.json?objectMask=mask[eventName,eventCreateDate,userType]&resultLimit=0,50&objectFilter={"eventCreateDate":{"operation":"greaterThanDate","options":[{"name":"date","value":["2021-03-01T00:00:00.0000-06:00"]}]}}'
```

Output example (first two events):
```json
[
    {
        "eventCreateDate": "2021-03-26T14:22:26.349808-06:00",
        "eventName": "Power On",
        "userType": "SYSTEM"
    },
    {
        "eventCreateDate": "2021-03-26T14:22:06.201563-06:00",
        "eventName": "Power Off",
        "userType": "SYSTEM"
    }
  ]

```

## [Get Event Log Names](#get-event-log-names) {#get-event-log-names .anchor-link}
To retrieve all event names We use [SoftLayer_Event_Log::getAllEventObjectNames](https://sldn.softlayer.com/reference/services/SoftLayer_Event_Log/getAllEventObjectNames/).
```bash
https://api.softlayer.com/rest/v3.1/SoftLayer_Event_Log/getAllEventObjectNames.json
```
```bash
curl -u $SL_USER:$SL_APIKEY 'https://api.softlayer.com/rest/v3.1/SoftLayer_Event_Log/getAllEventObjectNames.json'

```
Output:
```bash
['Bare Metal Instance',
 'Server',
 'API Authentication',
 'Security Group',
 'Account',
 'CDN',
 'User',
 'CCI',
 'Facility',
 'Cloud Object Storage',
 'Image',
 'Storage',
 'Bluemix LB']
```

## [Event Log User Types](#event-log-user-types) {#event-log-user-types .anchor-link}
To retrieve all user types We use [SoftLayer_Event_Log::getAllUserTypes](https://sldn.softlayer.com/reference/services/SoftLayer_Event_Log/getAllUserTypes/).
```bash
https://api.softlayer.com/rest/v3.1/SoftLayer_Event_Log/getAllUserTypes.json
```
  
```bash
curl -u $SL_USER:$SL_APIKEY 'https://api.softlayer.com/rest/v3.1/SoftLayer_Event_Log/getAllUserTypes.json'

```
Output:
```bash
    ['CUSTOMER', 'EMPLOYEE', 'SYSTEM']
```

## [Get System Logs](#get-system-logs) {#get-system-logs .anchor-link}

To retrieve all the SYSTEM logs events.
```bash
https://api.softlayer.com/rest/v3.1/SoftLayer_Event_Log/getAllObjects.json?
            resultLimit=0,50&
            objectMask=mask[eventName,eventCreateDate,userType]&
            objectFilter={"userType":{"operation":"SYSTEM"}}

```
    
```bash
curl -g -u $SL_USER:$SL_APIKEY 'https://api.softlayer.com/rest/v3.1/SoftLayer_Event_Log/getAllObjects.json?objectMask=mask[eventName,eventCreateDate,userType]&resultLimit=0,50&objectFilter={"userType":+{"operation":+"SYSTEM"}}'
```

Output example (first two events):
```json
[
    {
        "eventCreateDate": "2021-03-19T14:10:28.976723-06:00",
        "eventName": "Disable Port",
        "userType": "SYSTEM"
    },
    {
        "eventCreateDate": "2021-03-19T14:09:19.531900-06:00",
        "eventName": "Cancel Service",
        "userType": "SYSTEM"
    }
]

```


## [Get Login Events](#get-login-events) {#get-login-events .anchor-link}

```bash
https://api.softlayer.com/rest/v3.1/SoftLayer_Event_Log/getAllObjects.json?
            resultLimit=0,50&
            objectMask=mask[eventName,eventCreateDate,userType]&
            objectFilter={"eventName":{"operation":"^= Login"}}
```


```bash
curl -g -u $SL_USER:$SL_APIKEY 'https://api.softlayer.com/rest/v3.1/SoftLayer_Event_Log/getAllObjects.json?objectMask=mask[eventName,eventCreateDate,userType]&resultLimit=0,50&objectFilter={"eventName":+{"operation":+"^=+Login"}}'
```

Output example (first two events):
```json
[
    {
        "eventCreateDate": "2021-03-29T15:17:21.073746-06:00",
        "eventName": "Login Successful",
        "userType": "CUSTOMER"
    },
    {
        "eventCreateDate": "2021-03-29T15:13:43.159343-06:00",
        "eventName": "Login Successful",
        "userType": "CUSTOMER"
    }  
]

```

