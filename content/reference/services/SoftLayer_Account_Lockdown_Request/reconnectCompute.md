---
title: "reconnectCompute"
description: "Takes the original disconnected lockdown event ID, and an optional reconnect date. If no reconnect date is passed with the API call, the account reconnection will happen immediately. Otherwise, the account reconnection will happen on the date given. The associated lockdown event will be unlocked and closed at that time. "
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

### [REST Example](#reconnectCompute-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#reconnectCompute-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account_Lockdown_Request/{SoftLayer_Account_Lockdown_RequestID}/reconnectCompute'
```
