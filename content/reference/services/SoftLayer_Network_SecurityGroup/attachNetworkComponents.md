---
title: "attachNetworkComponents"
description: "Attach virtual guest network components to a security group by creating [SoftLayer_Virtual_Network_SecurityGroup_NetworkComponentBinding](/reference/datatypes/SoftLayer_Virtual_Network_SecurityGroup_NetworkComponentBinding) objects. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_SecurityGroup"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_SecurityGroup"
---

# [REST Example](#attachNetworkComponents-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#attachNetworkComponents-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [int]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_SecurityGroup/{SoftLayer_Network_SecurityGroupID}/attachNetworkComponents'
```
