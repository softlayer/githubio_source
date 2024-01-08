---
title: "getAllTicketStatuses"
description: "getAllTicketStatuses() retrieves a list of all statuses that a ticket may exist in. Ticket status represent the current state of a ticket, usually 'open', 'assigned', and 'closed'. 

Every SoftLayer ticket has statusId and status properties that correspond to one of the statuses returned by getAllTicketStatuses(). "
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

### [REST Example](#getAllTicketStatuses-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getAllTicketStatuses-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Ticket/getAllTicketStatuses'
```
