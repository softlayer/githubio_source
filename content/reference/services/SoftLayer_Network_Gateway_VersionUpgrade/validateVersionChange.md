---
title: "validateVersionChange"
description: ""
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Gateway_VersionUpgrade"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Gateway_VersionUpgrade"
---

# [REST Example](#validateVersionChange-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#validateVersionChange-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [int, int]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Gateway_VersionUpgrade/{SoftLayer_Network_Gateway_VersionUpgradeID}/validateVersionChange'
```
