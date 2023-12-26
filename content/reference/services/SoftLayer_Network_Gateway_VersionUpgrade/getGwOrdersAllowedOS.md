---
title: "getGwOrdersAllowedOS"
description: "Used to get a list per package of prices ids for allowed vSRX or vFSA OS-es for new orders. 

"
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

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [int, string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Gateway_VersionUpgrade/getGwOrdersAllowedOS'
```
