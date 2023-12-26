---
title: "getNetworkAddress"
description: "Retrieve a list of SoftLayer datacenter addresses."
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account_Address"
type: "reference"
layout: "method"
mainService : "SoftLayer_Account_Address"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account_Address/getNetworkAddress'
```
