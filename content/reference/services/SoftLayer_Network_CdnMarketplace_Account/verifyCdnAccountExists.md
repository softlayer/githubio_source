---
title: "verifyCdnAccountExists"
description: "Wrapper for UI to verify whether or not an account exists for user under specified vendor. Returns true if account exists, else false. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_CdnMarketplace_Account"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_CdnMarketplace_Account"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_CdnMarketplace_Account/verifyCdnAccountExists'
```
