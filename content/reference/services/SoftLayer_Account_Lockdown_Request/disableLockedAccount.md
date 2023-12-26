---
title: "disableLockedAccount"
description: "Takes the original lockdown request ID, and an optional disable date. If no date is passed with the API call, the account will be disabled immediately. Otherwise, the account will be disabled on the date given. All hardware will be reclaimed and all accounts permanently disabled. "
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

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account_Lockdown_Request/{SoftLayer_Account_Lockdown_RequestID}/disableLockedAccount'
```
