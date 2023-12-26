---
title: "getHasR1softBareMetalRestorePluginFlag"
description: "Return 1 if one of the account's hardware has an installation of R1Soft CDP otherwise 0."
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
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account/{SoftLayer_AccountID}/getHasR1softBareMetalRestorePluginFlag'
```
