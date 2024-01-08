---
title: "cancelRequest"
description: "Will cancel a lockdown request scheduled in the future. Once canceled, the lockdown request cannot be reconciled and new requests must be made for subsequent actions on the account. "
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

### [REST Example](#cancelRequest-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#cancelRequest-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account_Lockdown_Request/{SoftLayer_Account_Lockdown_RequestID}/cancelRequest'
```
