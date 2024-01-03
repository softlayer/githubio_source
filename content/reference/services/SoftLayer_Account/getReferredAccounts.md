---
title: "getReferredAccounts"
description: "If this is a account is a referral partner, the accounts this referral partner has referred"
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

# [REST Example](#getReferredAccounts-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getReferredAccounts-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account/{SoftLayer_AccountID}/getReferredAccounts'
```
