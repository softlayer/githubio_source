---
title: "getAccountHistory"
description: "Provides a history of an account's lockdown requests and their status."
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account_Lockdown_Request"
type: "reference"
layout: "method"
mainService : "SoftLayer_Account_Lockdown_Request"
---

# [REST Example](#getAccountHistory-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getAccountHistory-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [int]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account_Lockdown_Request/getAccountHistory'
```
