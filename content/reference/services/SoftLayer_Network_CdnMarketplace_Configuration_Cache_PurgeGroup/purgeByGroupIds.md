---
title: "purgeByGroupIds"
description: "This method purges the content from purge groups. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_CdnMarketplace_Configuration_Cache_PurgeGroup"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_CdnMarketplace_Configuration_Cache_PurgeGroup"
---

### [REST Example](#purgeByGroupIds-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#purgeByGroupIds-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string, string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_CdnMarketplace_Configuration_Cache_PurgeGroup/purgeByGroupIds'
```
