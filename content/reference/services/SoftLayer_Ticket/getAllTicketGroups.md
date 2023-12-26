---
title: "getAllTicketGroups"
description: "getAllTicketGroups() retrieves a list of all groups that a ticket may be assigned to. Ticket groups represent the internal department at SoftLayer who a ticket is assigned to. 

Every SoftLayer ticket has groupId and ticketGroup properties that correspond to one of the groups returned by getAllTicketGroups(). "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Ticket"
classes:
    - "SoftLayer_Ticket"
type: "reference"
layout: "method"
mainService : "SoftLayer_Ticket"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Ticket/getAllTicketGroups'
```
