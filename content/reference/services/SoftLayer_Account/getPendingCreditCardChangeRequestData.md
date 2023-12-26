---
title: "getPendingCreditCardChangeRequestData"
description: "Before being approved for general use, a credit card must be approved by a SoftLayer agent. Once a credit card change request has been either approved or denied, the change request will no longer appear in the list of pending change requests. This method will return a list of all pending change requests as well as a portion of the data from the original request. "
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
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account/getPendingCreditCardChangeRequestData'
```
