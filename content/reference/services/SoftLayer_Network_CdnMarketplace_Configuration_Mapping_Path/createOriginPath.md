---
title: "createOriginPath"
description: "SOAP API will create Origin Path for an existing CDN mapping and for a particular customer. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_CdnMarketplace_Configuration_Mapping_Path"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_CdnMarketplace_Configuration_Mapping_Path"
---

### [REST Example](#createOriginPath-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#createOriginPath-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Container_Network_CdnMarketplace_Configuration_Input]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_CdnMarketplace_Configuration_Mapping_Path/createOriginPath'
```
