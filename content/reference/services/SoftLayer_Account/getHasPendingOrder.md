---
title: "getHasPendingOrder"
description: "The number of orders in a PENDING status for a SoftLayer customer account."
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

### [REST Example](#getHasPendingOrder-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getHasPendingOrder-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account/{SoftLayer_AccountID}/getHasPendingOrder'
```
