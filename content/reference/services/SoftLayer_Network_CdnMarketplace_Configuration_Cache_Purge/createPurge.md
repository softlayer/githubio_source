---
title: "createPurge"
description: "This method creates a purge record in the purge table, and also initiates the create purge call. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_CdnMarketplace_Configuration_Cache_Purge"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_CdnMarketplace_Configuration_Cache_Purge"
---

### [REST Example](#createPurge-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#createPurge-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string, string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_CdnMarketplace_Configuration_Cache_Purge/createPurge'
```
