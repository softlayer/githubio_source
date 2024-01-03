---
title: "createObject"
description: "Create a new hardware member on the gateway. This also asynchronously sets up the network for this member. Progress of this process can be monitored via the gateway status. All members created with this object must have no VLANs attached. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Gateway_Member"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Gateway_Member"
---

# [REST Example](#createObject-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#createObject-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Network_Gateway_Member]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Gateway_Member/createObject'
```
