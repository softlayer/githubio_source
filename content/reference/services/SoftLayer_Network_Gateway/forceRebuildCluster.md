---
title: "forceRebuildCluster"
description: "Purpose is to rebuild the target Gateway cluster with the specified OS price id. Method will remove the current OS and apply the default configuration settings. This will result in an extended OUTAGE!! Any custom configuration settings must be re-applied after the forced rebuild is completed. This is a DESTRUCTIVE action, use with caution. 

"
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Gateway"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Gateway"
---

# [REST Example](#forceRebuildCluster-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#forceRebuildCluster-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [int]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Gateway/{SoftLayer_Network_GatewayID}/forceRebuildCluster'
```
