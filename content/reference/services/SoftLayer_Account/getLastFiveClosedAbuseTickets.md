---
title: "getLastFiveClosedAbuseTickets"
description: "The five most recently closed abuse tickets associated with an account."
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

### [REST Example](#getLastFiveClosedAbuseTickets-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getLastFiveClosedAbuseTickets-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account/{SoftLayer_AccountID}/getLastFiveClosedAbuseTickets'
```
