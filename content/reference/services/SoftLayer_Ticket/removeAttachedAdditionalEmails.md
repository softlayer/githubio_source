---
title: "removeAttachedAdditionalEmails"
description: "removeAttachedAdditionalEmails() removes the specified email addresses from a ticket's notification list. If one of the provided email addresses is not attached to the ticket then ''removeAttachedAdditiaonalEmails()'' ignores it and continues to the next one. Once the email addresses are removed ''removeAttachedAdditiaonalEmails()'' returns a boolean true. "
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
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Ticket/{SoftLayer_TicketID}/removeAttachedAdditionalEmails'
```
