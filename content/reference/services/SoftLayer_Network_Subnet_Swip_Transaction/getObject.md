---
title: "getObject"
description: "
**DEPRECATED**
getObject retrieves the SoftLayer_Network_Subnet_Swip_Transaction object whose ID number corresponds to the ID number of the init parameter passed to the SoftLayer_Network_Subnet_Swip_transaction service. You can only retrieve Swip transactions tied to the account. "
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

# [REST Example](#getObject-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getObject-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Subnet_Swip_Transaction/{SoftLayer_Network_Subnet_Swip_TransactionID}/getObject'
```
