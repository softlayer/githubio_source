---
title: "getOrphanBillingItems"
description: "The billing items that have no parent billing item. These are items that don't necessarily belong to a single server."
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

# [REST Example](#getOrphanBillingItems-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getOrphanBillingItems-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account/{SoftLayer_AccountID}/getOrphanBillingItems'
```
