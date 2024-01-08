---
title: "getAllObjects"
description: "Retrieve all possible ticket subjects. The SoftLayer customer portal uses this method in the add standard support ticket form."
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

### [REST Example](#getAllObjects-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getAllObjects-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Ticket_Subject/getAllObjects'
```
