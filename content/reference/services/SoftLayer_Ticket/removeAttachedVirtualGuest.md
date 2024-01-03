---
title: "removeAttachedVirtualGuest"
description: "Detach the given CloudLayer Computing Instance from a SoftLayer ticket. Removing an attachment may delay ticket processing time if the instance removed is relevant to the ticket's issue. Return a boolean true upon successful detachment. "
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

# [REST Example](#removeAttachedVirtualGuest-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#removeAttachedVirtualGuest-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [int]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Ticket/{SoftLayer_TicketID}/removeAttachedVirtualGuest'
```
