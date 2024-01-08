---
title: "validateByAccountAndCountryId"
description: "Will validate a PACT or WBS account ID and BMS country ID. If the record is invalid, an exception is thrown. Otherwise, a container with account information is returned. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account_Internal_Ibm_CostRecovery_Validator"
type: "reference"
layout: "method"
mainService : "SoftLayer_Account_Internal_Ibm_CostRecovery_Validator"
---

### [REST Example](#validateByAccountAndCountryId-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#validateByAccountAndCountryId-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string, string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account_Internal_Ibm_CostRecovery_Validator/validateByAccountAndCountryId'
```
