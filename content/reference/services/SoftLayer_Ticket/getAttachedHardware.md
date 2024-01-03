---
title: "getAttachedHardware"
description: "The hardware associated with a ticket. This is used in cases where a ticket is directly associated with one or more pieces of hardware."
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

# [REST Example](#getAttachedHardware-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getAttachedHardware-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Ticket/{SoftLayer_TicketID}/getAttachedHardware'
```
