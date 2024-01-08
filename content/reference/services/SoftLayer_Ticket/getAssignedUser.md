---
title: "getAssignedUser"
description: "The portal user that a ticket is assigned to."
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

### [REST Example](#getAssignedUser-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getAssignedUser-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Ticket/{SoftLayer_TicketID}/getAssignedUser'
```
