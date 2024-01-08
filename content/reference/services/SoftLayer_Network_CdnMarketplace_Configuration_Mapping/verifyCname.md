---
title: "verifyCname"
description: "Verifies the CNAME is Unique in the domain. The method will return true if CNAME is unique else returns false "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_CdnMarketplace_Configuration_Mapping"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_CdnMarketplace_Configuration_Mapping"
---

### [REST Example](#verifyCname-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#verifyCname-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_CdnMarketplace_Configuration_Mapping/verifyCname'
```
