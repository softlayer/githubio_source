---
title: "syncCurrentUserPopulationWithPaas"
description: "This method manually starts a synchronize operation for the current IBMid-authenticated user population of a linked account pair. 'Manually' means 'independent of an account link operation'. "
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

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account/syncCurrentUserPopulationWithPaas'
```
