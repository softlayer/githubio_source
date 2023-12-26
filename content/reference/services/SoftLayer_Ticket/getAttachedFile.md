---
title: "getAttachedFile"
description: "Retrieve the file attached to a SoftLayer ticket by it's given identifier. To retrieve a list of files attached to a ticket either call the SoftLayer_Ticket::getAttachedFiles method or call SoftLayer_Ticket::getObject with ''attachedFiles'' defined in an object mask. "
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
'https://api.softlayer.com/rest/v3.1/SoftLayer_Ticket/{SoftLayer_TicketID}/getAttachedFile'
```
