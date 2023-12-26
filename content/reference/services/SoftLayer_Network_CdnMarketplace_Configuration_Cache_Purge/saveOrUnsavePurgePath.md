---
title: "saveOrUnsavePurgePath"
description: "Creates a new saved purge if a purge path is saved. Deletes a saved purge record if the path is unsaved. "
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

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string, string, int]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_CdnMarketplace_Configuration_Cache_Purge/saveOrUnsavePurgePath'
```
