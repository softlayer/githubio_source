---
title: "getOrderEligibility"
description: "See [SoftLayer_Account::getOrderEligibilityServiceOrderTypes](/reference/services/SoftLayer_Account/getOrderEligibilityServiceOrderTypes) for the order type values available. 

Some packages may also require a resource type. See [SoftLayer_Account::getOrderEligibilityServiceResourceTypes](/reference/services/SoftLayer_Account/getOrderEligibilityServiceResourceTypes) for the values available. "
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

### [REST Example](#getOrderEligibility-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getOrderEligibility-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [int, string, string, boolean]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account/getOrderEligibility'
```
