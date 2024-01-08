---
title: "getTicketsClosedSinceDate"
description: "Retrieve all tickets closed since a given date. "
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

### [REST Example](#getTicketsClosedSinceDate-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getTicketsClosedSinceDate-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [dateTime]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Ticket/getTicketsClosedSinceDate'
```
