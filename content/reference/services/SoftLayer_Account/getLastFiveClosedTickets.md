---
title: "getLastFiveClosedTickets"
description: "The five most recently closed tickets associated with an account."
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account"
type: "reference"
layout: "method"
mainService : "SoftLayer_Account"
---

### [REST Example](#getLastFiveClosedTickets-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getLastFiveClosedTickets-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account/{SoftLayer_AccountID}/getLastFiveClosedTickets'
```
