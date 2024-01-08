---
title: "getFirstAttachedResource"
description: "The first physical or virtual server attached to a ticket."
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

### [REST Example](#getFirstAttachedResource-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getFirstAttachedResource-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Ticket/{SoftLayer_TicketID}/getFirstAttachedResource'
```
