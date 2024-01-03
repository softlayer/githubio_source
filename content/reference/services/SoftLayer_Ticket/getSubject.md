---
title: "getSubject"
description: "A ticket's subject. Only standard support tickets have an associated subject. A standard support ticket's title corresponds with it's subject's name."
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

# [REST Example](#getSubject-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getSubject-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Ticket/{SoftLayer_TicketID}/getSubject'
```
