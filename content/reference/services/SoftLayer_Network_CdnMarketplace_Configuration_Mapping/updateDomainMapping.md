---
title: "updateDomainMapping"
description: "SOAP API will update the Domain Mapping identified by the Unique Id. Following fields are allowed to be changed: originHost, HttpPort/HttpsPort, RespectHeaders, ServeStale 

Additionally, bucketName and fileExtension if OriginType is Object Store "
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

# [REST Example](#updateDomainMapping-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#updateDomainMapping-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Container_Network_CdnMarketplace_Configuration_Input]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_CdnMarketplace_Configuration_Mapping/updateDomainMapping'
```
