---
title: "getPendingInvoiceTotalOneTimeAmount"
description: "The total one-time charges for an account's pending invoice, if one exists. In other words, it is the sum of one-time charges, setup fees, and labor fees. It does not include taxes."
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
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account/{SoftLayer_AccountID}/getPendingInvoiceTotalOneTimeAmount'
```
