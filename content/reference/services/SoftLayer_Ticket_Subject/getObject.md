---
title: "getObject"
description: "getObject retrieves the SoftLayer_Ticket_Subject object whose ID number corresponds to the ID number of the init parameter passed to the SoftLayer_Ticket_Subject service. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Ticket"
classes:
    - "SoftLayer_Ticket_Subject"
type: "reference"
layout: "method"
mainService : "SoftLayer_Ticket_Subject"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Ticket_Subject/{SoftLayer_Ticket_SubjectID}/getObject'
```
