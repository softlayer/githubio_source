---
title: "getReverseDomainRecords"
description: "Retrieve all reverse DNS records associated with a subnet. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Subnet"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Subnet"
---

### [REST Example](#getReverseDomainRecords-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getReverseDomainRecords-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Subnet/{SoftLayer_Network_SubnetID}/getReverseDomainRecords'
```
