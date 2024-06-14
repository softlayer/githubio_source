---
title: "disconnectCompute"
description: "Takes an account ID. Note the disconnection will happen immediately. A brand account request ID will be returned and will then be updated when the disconnection occurs. "
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

### [REST Example](#disconnectCompute-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#disconnectCompute-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [int, string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account_Lockdown_Request/disconnectCompute'
```
