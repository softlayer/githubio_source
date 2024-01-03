---
title: "isActiveVmwareCustomer"
description: "Determines if the account is considered an active VMware customer and as such eligible to order VMware restricted products. This result is cached for up to 60 seconds. "
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

# [REST Example](#isActiveVmwareCustomer-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#isActiveVmwareCustomer-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account/isActiveVmwareCustomer'
```
