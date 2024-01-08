---
title: "removeSwipData"
description: "
**DEPRECATED**
This function, when called on an instantiated SWIP transaction, will allow you to start a 'DELETE' transaction with ARIN, allowing you to remove your SWIP registration information. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Subnet_Swip_Transaction"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Subnet_Swip_Transaction"
---

### [REST Example](#removeSwipData-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#removeSwipData-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Subnet_Swip_Transaction/{SoftLayer_Network_Subnet_Swip_TransactionID}/removeSwipData'
```
