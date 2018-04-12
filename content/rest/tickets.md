---
title: "Tickets"
description: "Examples of how to use and interact with tickets"
date: "2018-04-10"
classes:
    - "SoftLayer_Ticket"
    - "SoftLayer_Ticket_Attachment_File"
tags:
    - "resultlimit"
    - "objectmask"
    - "objectfilter"
    - "ticket"
---



# Tickets
Tickets are how SoftLayer and you communicate and resolve problems. They can be about anything from general questions, requests for upgrades, monitoring alerts, or anything else that might come up.


## Viewing Tickets
To start off, lets see how to go about getting tickets that already exist on our account. There are a variety of helper functions on the [SoftLayer_Account](/reference/services/SoftLayer_Account/) service that deal with tickets, and they all work basically the same way.  [SoftLayer_Account::getTickets](reference/services/SoftLayer_Account/getTickets/) and [SoftLayer_Account::getOpenTickets](reference/services/SoftLayer_Account/getOpenTickets/) are the most basic of these. 

```
curl -u $SL_USER:$SL_APIKEY -X GET -H "Accept: */*" -H "Accept-Encoding: gzip, deflate, compress"  'https://api.softlayer.com/rest/v3.1/SoftLayer_Account/getOpenTickets.json'
```

Output:
```
[
    {
        "accountId": 307608,
        "assignedUserId": 244956,
        "createDate": "2018-03-30T14:41:47-06:00",
        "groupId": 1004,
        "id": 57894695,
        "lastEditDate": null,
        "lastEditType": "USER",
        "lastResponseDate": "2018-03-30T14:41:48-06:00",
        "modifyDate": "2018-03-30T14:41:48-06:00",
        "notifyUserOnUpdateFlag": false,
        "priority": 0,
        "status": {
            "id": 1001,
            "name": "Open"
        },
        "statusId": 1001,
        "subjectId": null,
        "title": "Virtual Server Cancellation - 03/30/18",
        "totalUpdateCount": 1,
        "userEditableFlag": true
    },
```

From there, the [SoftLayer_Ticket](/reference/datatypes/SoftLayer_Ticket/) datatype has quite a few fields we might be interested in.  Here is how you would get the updates for the ticket, along with whatever hardware was attached.


https://api.softlayer.com/rest/v3.1/SoftLayer_Account/getOpenTickets.json?
objectMask=mask[id, title, updates, attachedHardware[hostname, id]]

> Reminder: When requesting a LOCAL property, the result will remove all local properties not specified. When requesting a RELATIONAL property, that property, along with any of its default properties, will be added

```
curl -u $SL_USER:$SL_APIKEY -X GET -H "Accept: */*" -H "Accept-Encoding: gzip, deflate, compress"  'https://api.softlayer.com/rest/v3.1/SoftLayer_Account/getOpenTickets.json?objectMask=mask%5Bid%2Ctitle%2Cupdates%2CattachedHardware%5Bhostname%2Cid%5D%5D'
```
 
Output:

```
   {
        "attachedHardware": [
            {
                "hostname": "fmirdal13",
                "id": 1477781
            }
        ],
        "id": 58043007,
        "title": "Server Cancellation - 04/04/2018",
        "updates": [
            {
                "createDate": "2018-04-03T09:38:36-06:00",
                "editorId": 205,
                "editorType": "AUTO",
                "entry": "A cancellation request has been submitted for the following:\nServer: fmirdal13.insomnia.com\nPublic IP: 169.60.129.46\nPrivate IP: 10.186.96.230\nServers and services must be cancelled prior to Apr 03, 2018 23:59:59 CDT.\n=================\nCustomer Note:\n",
                "id": 358332963,
                "ticketId": 58043007
            }
        ]
    },
```


To get information about just one ticket, the [SoftLayer_Ticket::getObject](/reference/services/SoftLayer_Ticket/getObject) method would be used.

```
curl -u $SL_USER:$SL_APIKEY -X GET -H "Accept: */*" -H "Accept-Encoding: gzip, deflate, compress"  'https://api.softlayer.com/rest/v3.1/SoftLayer_Ticket/58043007/getObject.json?objectMask=mask%5Bid%2Ctitle%2Cupdates%2CattachedHardware%5Bhostname%2Cid%5D%5D'
```

## Creating Tickets
There are a few create options in the SoftLayer_Ticket service, the only difference being which internal group they get routed to, and should be obvious based on the method name which one you need. If in doubt, use the standard ticket, [SoftLayer_Ticket::createStandardTicket](reference/services/SoftLayer_Ticket/createStandardTicket/)

The bare minimum to create a ticket is the following command:
```
curl -u $SL_USER:$SL_APIKEY -X POST -H "Accept: */*" -H "Accept-Encoding: gzip, deflate, compress" -d '{"parameters": [{"subjectId": 1021}, "Content of the ticket goes here"]}' 'https://api.softlayer.com/rest/v3.1/SoftLayer_Ticket/createStandardTicket.json'
```

The result you get back will be a ticket object. [This example](/python/create_ticket/) has some information about which ticket subjects match up with which Ids. The whole list can be retrieved with this call.

```
curl -u $SL_USER:$SL_APIKEY -X GET -H "Accept: */*" -H "Accept-Encoding: gzip, deflate, compress"  'https://api.softlayer.com/rest/v3.1/SoftLayer_Ticket_Subject/getAllObjects.json'
```


The `parameters` array passed into the createStandardTicket method matches the order shown in the documentation for that method.

Another example

```
curl -u $SL_USER:$SL_APIKEY -X POST -H "Accept: */*" -H "Accept-Encoding: gzip, deflate, compress" -d '{"parameters": [{"subjectId": 1021, "title": "Test API Ticket"}, "Content of the ticket goes here", 305250,"FakePass","Test",22,"HARDWARE"]}' 'https://api.softlayer.com/rest/v3.1/SoftLayer_Ticket/createStandardTicket.json'
```


## Updating Tickets

Once a ticket is created, you may want to update it to respond to another update, or add more information. This is done through the [SoftLayer_Ticket::addUpdate](/reference/services/SoftLayer_Ticket/addUpdate/) method.


```
curl -u $SL_USER:$SL_APIKEY -X POST -H "Accept: */*" -H "Accept-Encoding: gzip, deflate, compress" -d '{"parameters": [{"entry": "Testing updates"}]}' 'https://api.softlayer.com/rest/v3.1/SoftLayer_Ticket/<TICKET ID YOU WANT TO UDPATE>/addUpdate.json'
```


## Attachments

### Attach Files
[SoftLayer_Ticket::addAttachedFile](/reference/services/SoftLayer_Ticket/addAttachedFile/) is useful when you need to add a screenshot, PDF, or something else thats not plain text to a ticket. 

Our ticket ID for this example is 58504963. 

>*NOTE* the `data` field MUST be base64 encoded, which can be tricky to do in bash. The base64 string needs to be enclosed with "", but bash needs the $(base64 <file>) bit to be escaped from the '' string.

```
curl -u $SL_USER:$SL_APIKEY -X POST -H "Accept: */*" -H "Accept-Encoding: gzip, deflate, compress" --data '{"parameters": [{"data": "'"$(base64 test.txt)"'", "filename": "test2.txt"}]}' 'https://api.softlayer.com/rest/v3.1/SoftLayer_Ticket/58504963/addAttachedFile'
```

### Attach Hardware
For the best response from Support, you should attach any relevant hardware or virtual guests to the ticket, so Support knows which servers you are specifically talking about. 

There are different methods if you want to attach a bare metal or virtual server, but they behave the same.

```
curl -u $SL_USER:$SL_APIKEY -X POST -H "Accept: */*" -H "Accept-Encoding: gzip, deflate, compress" --data '{"parameters": [481966]}' 'https://api.softlayer.com/rest/v3.1/SoftLayer_Ticket/58504963/addAttachedHardware'

curl -u $SL_USER:$SL_APIKEY -X POST -H "Accept: */*" -H "Accept-Encoding: gzip, deflate, compress" --data '{"parameters": [27500547]}' 'https://api.softlayer.com/rest/v3.1/SoftLayer_Ticket/58504963/addAttachedVirtualGuest'
```




## Final Bits
Hopefully that helps explain most of the actions you can do with tickets. 

