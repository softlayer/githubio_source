---
title: "getObject"
description: "getObject retrieves the SoftLayer_Ticket object whose ID number corresponds to the ID number of the init parameter passed to the SoftLayer_Ticket service. You can only retrieve tickets that are associated with your SoftLayer customer account. "
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
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Ticket/{SoftLayer_TicketID}/getObject'
```
