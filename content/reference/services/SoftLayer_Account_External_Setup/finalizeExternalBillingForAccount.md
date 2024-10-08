---
title: "finalizeExternalBillingForAccount"
description: "Calling this method signals that the account with the provided account id is ready to be billed by the external billing system. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account_External_Setup"
type: "reference"
layout: "method"
mainService : "SoftLayer_Account_External_Setup"
---

### [REST Example](#finalizeExternalBillingForAccount-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#finalizeExternalBillingForAccount-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [int]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account_External_Setup/finalizeExternalBillingForAccount'
```
