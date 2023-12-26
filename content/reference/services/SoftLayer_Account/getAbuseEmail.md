---
title: "getAbuseEmail"
description: "An email address that is responsible for abuse and legal inquiries on behalf of an account. For instance, new legal and abuse tickets are sent to this address."
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
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account/{SoftLayer_AccountID}/getAbuseEmail'
```
