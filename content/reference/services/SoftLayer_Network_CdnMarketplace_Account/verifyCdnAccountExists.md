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

# [REST Example](#verifyCdnAccountExists-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#verifyCdnAccountExists-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_CdnMarketplace_Account/verifyCdnAccountExists'
```
