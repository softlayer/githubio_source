---
title: "addAttachedVirtualGuest"
description: "Attach the given CloudLayer Computing Instance to a SoftLayer ticket. An attachment provides an easy way for SoftLayer's employees to quickly look up your records in the case of specific issues. "
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
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [int, boolean]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Ticket/{SoftLayer_TicketID}/addAttachedVirtualGuest'
```
