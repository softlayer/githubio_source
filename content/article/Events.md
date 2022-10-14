---
title: "Events and Notifications"
description: "How to manage Event Notifications through the API. Covers both monitoring and maintenance events, and how configure which email addresses get notified about these events."
date: "2022-10-14"
tags:
    - "article"
    - "sldn"
---


# The Basics

There are two types of Events that the SoftLayer API deals with.

1. Maintenance Events

These are the Classic Infrastructure [Planned](https://cloud.ibm.com/classic/event/planned), [Unplanned](https://cloud.ibm.com/classic/event/unplanned) and [Announcement](https://cloud.ibm.com/classic/event/announcement) events in the portal. These events *DO NOT* include other cloud.ibm.com services and notifications. *ONLY* classic infrastructure.

2. Monitoring Events

These are the Hardware and Virtual monitoring events that will let you know if a server has gone down/up.

From the API perspective, these are two separate things, but we will talk about them both in this article since both events can trigger an email alert that we will want to configure.


# Maintenance Events

We interact with these events through the [Notification_Occurrence_Event Service](https://sldn.softlayer.com/reference/services/SoftLayer_Notification_Occurrence_Event/). The [getAllObjects](https://sldn.softlayer.com/reference/services/SoftLayer_Notification_Occurrence_Event/getAllObjects/) method is the best place to start. By default this method will return all Events ever created on your account, so we will need to use an [objectFilter](/article/object-filters) to limit the results to only events we care about.

## API Example


```bash
curl -u $SL_USER:$SL_APIKEY  'https://api.softlayer.com/rest/v3.1/SoftLayer_Notification_Occurrence_Event/getAllObjects.json?objectMask=mask[id, subject, startDate, endDate, modifyDate, statusCode, acknowledgedFlag, impactedResourceCount, updateCount, systemTicketId, notificationOccurrenceEventType[keyName]]&objectFilter={"notificationOccurrenceEventType": {"keyName": {"operation": "PLANNED"}}, "endDate": {"operation": "> sysdate - 2"}, "startDate": {"operation": "orderBy", "options": [{"name": "sort", "value": ["DESC"]}]}}&resultLimit=0,100'
```

This will get use all the events on our account, and selects the following [SoftLayer_Notification_Occurrence_Event Properties](https://sldn.softlayer.com/reference/datatypes/SoftLayer_Notification_Occurrence_Event/)
```python
objectMask = mask[
    id, subject, startDate, endDate, modifyDate, statusCode, acknowledgedFlag, impactedResourceCount,
    updateCount, systemTicketId, notificationOccurrenceEventType[keyName]
]
```

Then this API example will filter the events so only events that are "PLANNED", have an endDate within 2 days, and ordered by startDate.

```python
objectFilter = {
    "notificationOccurrenceEventType": {"keyName": {"operation": "PLANNED"}},
    "endDate": {"operation": "> sysdate - 2"}, 
    "startDate": {"operation": "orderBy", "options": [{"name": "sort", "value": ["DESC"]}]}}
```

With a slight change to the objectFilter, we can get UNPLANNED_INCIDENT events. Notice we changed the event type, and instead of `endDate` we use `modifyDate` for these because UNPLANNED_INCIDENTS don't really have an endDate property filled out. I'm not sure why. 

We also used an absolute date (`10-04-2022`) as an example on how to use that format. For these Events its important to use the MM-DD-YYYY format for dates instead of the usualy MM/DD/YY format used in other parts of the API.

```python
objectFilter = {
    "notificationOccurrenceEventType": {"keyName": {"operation": "UNPLANNED_INCIDENT"}}, 
    "modifyDate": {"operation": "greaterThanDate", "options": [{"name":"date", "value": ["10-04-2022"]}]}, 
    "startDate": {"operation": "orderBy", "options": [{"name": "sort", "value": ["DESC"]}]}}
```


## CLI Example

The [slcli](https://softlayer-python.readthedocs.io/en/latest/cli/account/#account-events) and [ibmcloud sl](https://cloud.ibm.com/docs/cli?topic=cli-getting-started) tools both have an events command that makes getting this information easy.

![Account Events](/img/articles/slci-account-events.png)

## Acknowledge Events

If you get tired of seeing "You have unread notifications" in the classic side of the portal, you can automatically "read/Acknowledge" these with the API.
![Account Notifications](/img/articles/account-notifications.png)

This `slcli` command will get all the unacknowledged events on your account. There may be a lot more than show up in the portal from stale events, but we might as well ack those as well.
```bash
slcli -vvv call-api SoftLayer_Notification_Occurrence_Event getAllObjects --mask="mask[id, subject, startDate, endDate, acknowledgedFlag]" --json-filter='{"acknowledgedFlag":{"operation":"0"},"startDate": {"operation": "orderBy", "options": [{"name": "sort", "value": ["DESC"]}]}}' --limit=50
```

Once we have the Event Id, we just need to call [SoftLayer_Notification_Occurrence_Event::acknowledgeNotification()](https://sldn.softlayer.com/reference/services/SoftLayer_Notification_Occurrence_Event/acknowledgeNotification/)
```bash
$  slcli -v call-api SoftLayer_Notification_Occurrence_Event acknowledgeNotification --id=353435
Calling: SoftLayer_Notification_Occurrence_Event::acknowledgeNotification(id=353435, mask='', filter='{}', args=(), limit=None, offset=None))
True
```

You can also use the `slcli` to do this with the following command:

```bash
slcli -v account events --ack-all
```

Also, when viewing events in the portal, the ID you are shown is NOT the SoftLayer_Notification_Occurrence_Event, but the Ticket id.
![systemTicketId](/img/articles/account-notifications-details.png)

In the screenshot, we see the `ID` is `149521921`, so if we want to find that Event, we can use the following API call.

```bash
# SLCLI Example
slcli -vvv call-api SoftLayer_Notification_Occurrence_Event getAllObjects --mask="mask[id, subject, startDate, endDate, acknowledgedFlag, systemTicketId]" --json-filter='{"systemTicketId":{"operation":"149521921"}}'
# Curl Example
curl -u $SL_USER:$SL_APIKEY -X GET -H "Accept: */*" -H "Accept-Encoding: gzip, deflate, compress"
'https://api.softlayer.com/rest/v3.1/SoftLayer_Notification_Occurrence_Event/getAllObjects.json?objectMask=mask%5Bid%2C+subject%2C+startDate%2C+endDate%2C+acknowledgedFlag%2C+systemTicketId%5D&objectFilter=%7B%22systemTicketId%22%3A+%7B%2
2operation%22%3A+%22149521921%22%7D%7D'
┌──────────────────┬───────────────────────────┬────────┬───────────────────────────┬─────────────────────────────────────────────────────────────────────────────────────┬────────────────┐
│ acknowledgedFlag │          endDate          │   id   │         startDate         │                                       subject                                       │ systemTicketId │
├──────────────────┼───────────────────────────┼────────┼───────────────────────────┼─────────────────────────────────────────────────────────────────────────────────────┼────────────────┤
│       True       │ 2022-10-24T00:00:00-06:00 │ 354139 │ 2022-10-23T12:00:00-06:00 │ Performance/Endurance File and Block Storage Services (PAR01) 23-Oct-2022 18:00 UTC │   149521921    │
└──────────────────┴───────────────────────────┴────────┴───────────────────────────┴─────────────────────────────────────────────────────────────────────────────────────┴────────────────┘

```


## Subscribing and Un-Subscribing to Events

In the portal, the [Notifications](https://cloud.ibm.com/user/notifications) page lets you set which things you want to be emailed for, but some of this can be configured in the Softlayer/Classic API as well. These will involve interacting with your User_Customer record, and you will need to know your ID for that. The following API call can easily get that information
```bash
# SLCLI
slcli -vvv call-api SoftLayer_Account getCurrentUser --mask="mask[id,username]"
┌──────────┬───────────┐
│     name │ value     │
├──────────┼───────────┤
│       id │ 167758    │
└──────────┴───────────┘
# Curl
curl -u $SL_USER:$SL_APIKEY -X GET -H "Accept: */*" -H "Accept-Encoding: gzip, deflate, compress"  'https://api.softlayer.com/rest/v3.1/SoftLayer_Account/getCurrentUser.json?objectMask=mask%5Bid%2Cusername%5D'
```

### Seeing your subscriptions

[SoftLayer_Email_Subscription::getAllObjects](https://sldn.softlayer.com/reference/services/SoftLayer_Email_Subscription/getAllObjects/) will show what notifications you are subscribed to.

```bash
# SLCLI
$ slcli -v user notifications
Calling: SoftLayer_Email_Subscription::getAllObjects(id=None, mask='mask[enabled]', filter='None', args=(), limit=None, offset=None))
┌────┬─────────────────────────────┬────────────────────────────────────────────────────────────────────────────────────────────────────────┬─────────┐
│ Id │ Name                        │ Description                                                                                            │ Enabled │
├────┼─────────────────────────────┼────────────────────────────────────────────────────────────────────────────────────────────────────────┼─────────┤
│ 1  │ Order Being Reviewed        │ Email about your order.                                                                                │ True    │
│ 8  │ High Impact                 │ Maintenances that will or are likely to cause service outages and disruptions                          │ False   │
│ 15 │ Major Impact                │ Important Events such as legal notices, service decommissions or security patches.                     │ False   │
│ 11 │ Severity 1                  │ Incidents that cause severe to catastrophic service disruptions affecting multiple customers.          │ False   │
│ 5  │ Provision Complete - VSI    │ Email when VSI provisioning is complete.                                                               │ False   │
│ 16 │ Minor Impact                │ Important announcements worth being informed including product enhancements.                           │ False   │
│ 12 │ Severity 2                  │  Incidents that cause measurable service degradation yet not an actual outage.                         │ False   │
│ 2  │ Order Approved              │ Email when your order is approved.                                                                     │ False   │
│ 9  │ Medium Impact               │ Maintenances that will or are likely to cause measurable service degradation yet not an actual outage. │ False   │
│ 6  │ Provision Complete - Server │ Email when server provisioning details is complete.                                                    │ False   │
│ 13 │ Severity 3                  │ Incidents with no evident service disruption due to redundancy.                                        │ False   │
│ 7  │ Reload Complete             │ Email sent when operating system reload is complete.                                                   │ False   │
│ 3  │ Order Approved - VSI        │ Email when your VSI order is approved.                                                                 │ False   │
│ 10 │ Low Impact                  │ Maintenances with no service disruption during or after the maintenance.                               │ False   │
│ 4  │ Order Approved - Server     │ Email when your server order is approved.                                                              │ False   │
│ 14 │ Severity 4                  │ A notable incident that does not impact services or operations in any way.                             │ False   │
└────┴─────────────────────────────┴────────────────────────────────────────────────────────────────────────────────────────────────────────┴─────────┘

# Curl
curl -u $SL_USER:$SL_APIKEY -X GET -H "Accept: */*" -H "Accept-Encoding: gzip, deflate, compress"  'https://api.softlayer.com/rest/v3.1/SoftLayer_Email_Subscription/getAllObjects.json?objectMask=mask%5Benabled%5D'
````

### Enable/Disabled a Subscription

This can easily be done with the Email_Subscription id you want to interact with, and the [SoftLayer_Email_Subscription::enable](https://sldn.softlayer.com/reference/services/SoftLayer_Email_Subscription/enable) and [SoftLayer_Email_Subscription::disable](https://sldn.softlayer.com/reference/services/SoftLayer_Email_Subscription/disable) API methods.

```bash
# SLCLI
slcli -vvv user edit-notifications --enable 'High Impact'
# CURL
curl -u $SL_USER:$SL_APIKEY -X GET -H "Accept: */*" -H "Accept-Encoding: gzip, deflate, compress"  'https://api.softlayer.com/rest/v3.1/SoftLayer_Email_Subscription/8/enable.json'
```

# Monitoring Events