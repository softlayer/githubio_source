---
title: "Creating a support ticket"
description: "Create a standard support ticket assigned to your user"
date: "2016-02-09"
classes: ["SoftLayer_Ticket_Subject", "SoftLayer_Ticket"]
tags:
    - "ticket"
---

Standard support tickets' titles must be selected from a pre-determined list of ticket subjects, defined in the [SoftLayer_Ticket_Subject](http://sldn.softlayer.com/reference/services/SoftLayer_Ticket_Subject) service. The following example will output all of the Ticket Subjects:

```python

import SoftLayer
from pprint import pprint as pp

client = SoftLayer.Client()
subjects = client['Ticket_Subject'].getAllObjects()
pp(subjects)

```

Once you have the Ticket Subject ID you can pass it to [createStandardTicket](http://sldn.softlayer.com/reference/services/SoftLayer_Ticket/createStandardTicket). In the following example we are opening a ticket under the subject Hardware Firewall Question (ID 1121).

```python

import SoftLayer
client = SoftLayer.Client()
currentUser = client['Account'].getCurrentUser()
new_ticket = {
       'subjectId': 1121,
       'assignedUserId': currentUser['id']
}
created_ticket = client['Ticket'].createStandardTicket(new_ticket, "Content of the ticket goes here")

```
