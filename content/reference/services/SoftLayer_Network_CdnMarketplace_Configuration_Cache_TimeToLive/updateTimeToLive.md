---
title: "updateTimeToLive"
description: "Updates an existing Time To Live object. If the old and new inputs are equal, exits early. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_CdnMarketplace_Configuration_Cache_TimeToLive"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_CdnMarketplace_Configuration_Cache_TimeToLive"
---

### [REST Example](#updateTimeToLive-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#updateTimeToLive-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string, string, string, string, string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_CdnMarketplace_Configuration_Cache_TimeToLive/updateTimeToLive'
```
