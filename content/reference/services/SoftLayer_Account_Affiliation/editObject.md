---
title: "editObject"
description: "Edit an affiliation that is associated to an existing account. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account_Affiliation"
type: "reference"
layout: "method"
mainService : "SoftLayer_Account_Affiliation"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Account_Affiliation]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account_Affiliation/{SoftLayer_Account_AffiliationID}/editObject'
```
