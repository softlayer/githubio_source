---
title: "resendSwipData"
description: "
**DEPRECATED**
This function will allow you to update ARIN's registration data for a subnet to your current RWHOIS data. "
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

### [REST Example](#resendSwipData-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#resendSwipData-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Subnet_Swip_Transaction/{SoftLayer_Network_Subnet_Swip_TransactionID}/resendSwipData'
```
