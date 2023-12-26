---
title: "getObject"
description: "getObject retrieves the SoftLayer_Account object whose ID number corresponds to the ID number of the init parameter passed to the SoftLayer_Account service. You can only retrieve the account that your portal user is assigned to. "
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
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account/getObject'
```
