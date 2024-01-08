---
title: "markAsViewed"
description: "Mark a ticket as viewed.  All currently posted updates will be marked as viewed. The lastViewedDate property will be updated to the current time. "
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

### [REST Example](#markAsViewed-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#markAsViewed-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Ticket/{SoftLayer_TicketID}/markAsViewed'
```
