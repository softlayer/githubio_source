---
title: "getTicketsClosedInTheLastThreeDays"
description: "Tickets closed within the last 72 hours or last 10 tickets, whichever is less, associated with an account."
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

# [REST Example](#getTicketsClosedInTheLastThreeDays-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getTicketsClosedInTheLastThreeDays-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account/{SoftLayer_AccountID}/getTicketsClosedInTheLastThreeDays'
```
