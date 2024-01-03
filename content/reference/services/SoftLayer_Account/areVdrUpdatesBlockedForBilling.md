---
title: "areVdrUpdatesBlockedForBilling"
description: "This method indicates whether or not Bandwidth Pooling updates are blocked for the account so the billing cycle can run.  Generally, accounts are restricted from moving servers in or out of Bandwidth Pools from 12:00 CST on the day prior to billing, until the billing batch completes, sometime after midnight the day of actual billing for the account. "
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

# [REST Example](#areVdrUpdatesBlockedForBilling-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#areVdrUpdatesBlockedForBilling-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account/areVdrUpdatesBlockedForBilling'
```
