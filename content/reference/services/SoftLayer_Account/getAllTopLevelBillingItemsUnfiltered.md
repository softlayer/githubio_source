---
title: "getAllTopLevelBillingItemsUnfiltered"
description: "The billing items that will be on an account's next invoice. Does not consider associated items."
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

# [REST Example](#getAllTopLevelBillingItemsUnfiltered-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getAllTopLevelBillingItemsUnfiltered-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account/{SoftLayer_AccountID}/getAllTopLevelBillingItemsUnfiltered'
```
