---
title: "managerApprove"
description: "Applies manager approval to a pending internal IBM account request. If cost recovery is already configured, this will create an account. If not, this will remind the internal team to configure cost recovery and create the account when possible. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account_Internal_Ibm"
type: "reference"
layout: "method"
mainService : "SoftLayer_Account_Internal_Ibm"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [int, string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account_Internal_Ibm/managerApprove'
```
