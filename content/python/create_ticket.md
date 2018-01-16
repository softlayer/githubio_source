---
title: "Creating a support ticket"
description: "Create a standard support ticket assigned to your user"
date: "2018-01-16"
classes: ["SoftLayer_Ticket_Subject", "SoftLayer_Ticket"]
tags:
    - "ticket"
---

## Getting Subjects
Standard support tickets' titles must be selected from a pre-determined list of ticket subjects, defined in the [SoftLayer_Ticket_Subject](http://sldn.softlayer.com/reference/services/SoftLayer_Ticket_Subject) service. The following example will output all of the Ticket Subjects:

```python

import SoftLayer
client = SoftLayer.Client()
def getSubjects(self):
    mask = "mask[group]"
    subjects = client.call('SoftLayer_Ticket_Subject', 'getAllObjects', mask=mask)
    print("|Subject Id | Subject Name | Group Name |")
    print("| --- | --- | --- |")
    for subject in subjects:
        print("|%s| %s| %s|" % (subject['id'], subject['name'], subject['group']['name']))

```

### Subjects
|Subject Id | Subject Name | Group Name |
| --- | --- | --- |
|1522| API Question| Support|
|1001| Accounting Request| Accounting|
|1181| CDN Question| SysAdmin|
|1261| Colocation Service Request| Hardware|
|1041| DNS Request| Support|
|1201| DOS/Abuse Issue| Support|
|1121| Hardware Firewall Question| Support|
|1021| Hardware Issue| Support|
|1122| Hardware Load Balancer Question| Support|
|1081| Licensing Question| Support|
|1141| Mail Server Issue| Support|
|1004| OS Reload Question| Support|
|1005| Portal Information Question| Support|
|1061| Private Network Question| Support|
|1022| Public Network Question| Support|
|1003| Reboots and Console Access| Support|
|1002| Sales Request| Sales|
|1603| Sales Request - Compute & Infrastructure| Sales|
|1645| Sales Request - Firewall Service| Sales|
|1647| Sales Request - General Question| Sales|
|1605| Sales Request - Network & Security Services| Sales|
|1643| Sales Request - Other Services| Sales|
|1607| Sales Request - Upgrades & Add-ons| Sales|
|1101| Security Issue| Support|
|1161| Storage Question| Support|
|1221| Transcoding Question| Support|
|1723| VMware Solutions| VMware Solutions|
|1482| Vyatta Question| SysAdmin|


## Creating Tickets

Once you have the Ticket Subject ID you can pass it to [createStandardTicket](http://sldn.softlayer.com/reference/services/SoftLayer_Ticket/createStandardTicket). In the following example we are opening a ticket under the subject Hardware Issue (ID 1021).

```python

import SoftLayer
client = SoftLayer.Client()
currentUser = client['Account'].getCurrentUser()
new_ticket = {
       'subjectId': 1021,
       'assignedUserId': currentUser['id']
}
created_ticket = client.call('SoftLayer_Ticket', 'createStandardTicket', new_ticket, "Content of the ticket goes here")

```


### Full Example
createStandardTicket takes a few arguments that can be used to create a ticket. Anything that isn't an argument to createStandardTicket should be passed in as the ticket template object. 

```python
import SoftLayer
client = SoftLayer.Client()
def createTicket(self):
    current_user = client.call('SoftLayer_Account', 'getCurrentUser')
    body = "I'm testing API ticket creation. Please close this ticket if you see it. Thanks."
    serverId = 1317535
    serverPass = '12345'
    # http://sldn.softlayer.com/reference/datatypes/SoftLayer_Ticket
    new_ticket = {
        'subjectId': 1021,
        'assignedUserId': current_user['id'],
        'title': 'TESTING TICKET 003',
        'priority': 4
    }
    # parameter list is from, need to be in order http://sldn.softlayer.com/reference/services/softlayer_ticket/createStandardTicket
    created_ticket = client.call('SoftLayer_Ticket', 'createStandardTicket', 
        new_ticket, body, serverId, serverPass, None, None, None, 'HARDWARE')
    pp(created_ticket)
```