---
title: "removeAttachedHardware"
description: "detach the given hardware from a SoftLayer ticket. Removing a hardware attachment may delay ticket processing time if the hardware removed is relevant to the ticket's issue. Return a boolean true upon successful hardware detachment. "
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
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [int]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Ticket/{SoftLayer_TicketID}/removeAttachedHardware'
```
