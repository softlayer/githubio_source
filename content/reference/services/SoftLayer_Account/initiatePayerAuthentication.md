---
title: "initiatePayerAuthentication"
description: "Initiates Payer Authentication and provides data that is required for payer authentication enrollment and device data collection. "
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
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Billing_Payment_Card_PayerAuthentication_Setup_Information]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account/initiatePayerAuthentication'
```
