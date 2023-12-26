---
title: "updateAttachedAdditionalEmails"
description: "Creates new additional emails for assigned user if new emails are provided. Attaches any newly created additional emails to ticket. Remove any additional emails from a ticket that are not provided as part of $emails "
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
'https://api.softlayer.com/rest/v3.1/SoftLayer_Ticket/{SoftLayer_TicketID}/updateAttachedAdditionalEmails'
```
