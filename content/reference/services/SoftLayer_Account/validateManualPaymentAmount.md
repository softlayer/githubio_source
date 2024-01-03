---
title: "validateManualPaymentAmount"
description: "This method checks global and account specific requirements and returns true if the dollar amount entered is acceptable for this account and false otherwise. Please note the dollar amount is in USD. "
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

# [REST Example](#validateManualPaymentAmount-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#validateManualPaymentAmount-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account/validateManualPaymentAmount'
```
