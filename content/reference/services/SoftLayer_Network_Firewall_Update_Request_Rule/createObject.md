---
title: "createObject"
description: "Create a new firewall update request. The SoftLayer_Network_Firewall_Update_Request object passed to this function must have at least one rule. 

''createObject'' returns a Boolean ''true'' on successful object creation or ''false'' if your firewall update request was unable to be created.. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Firewall_Update_Request_Rule"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Firewall_Update_Request_Rule"
---

# [REST Example](#createObject-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#createObject-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Network_Firewall_Update_Request_Rule]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Firewall_Update_Request_Rule/createObject'
```
