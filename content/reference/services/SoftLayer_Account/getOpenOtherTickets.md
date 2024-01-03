---
title: "getOpenOtherTickets"
description: "The open tickets that do not belong to the abuse, accounting, sales, or support groups associated with an account."
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

# [REST Example](#getOpenOtherTickets-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getOpenOtherTickets-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account/{SoftLayer_AccountID}/getOpenOtherTickets'
```
