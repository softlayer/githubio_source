---
title: "verifyDomainMapping"
description: "Verifies the status of the domain mapping by calling the rest api; will update the status, cname, and vendorCName if necessary and will return the updated values. "
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

### [REST Example](#verifyDomainMapping-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#verifyDomainMapping-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [int]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_CdnMarketplace_Configuration_Mapping/verifyDomainMapping'
```
