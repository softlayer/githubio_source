---
title: "addAttachedDedicatedHost"
description: "Attach the given Dedicated Host to a SoftLayer ticket. An attachment provides an easy way for SoftLayer's employees to quickly look up your records in the case of specific issues. "
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

# [REST Example](#addAttachedDedicatedHost-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#addAttachedDedicatedHost-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [int]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Ticket/{SoftLayer_TicketID}/addAttachedDedicatedHost'
```
