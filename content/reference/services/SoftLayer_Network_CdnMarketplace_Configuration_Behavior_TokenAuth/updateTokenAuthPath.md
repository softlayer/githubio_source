---
title: "updateTokenAuthPath"
description: "SOAP API will update Token authentication Path for an existing mapping and for a particular customer. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_CdnMarketplace_Configuration_Behavior_TokenAuth"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_CdnMarketplace_Configuration_Behavior_TokenAuth"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Container_Network_CdnMarketplace_Configuration_Behavior_TokenAuth]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_CdnMarketplace_Configuration_Behavior_TokenAuth/updateTokenAuthPath'
```
