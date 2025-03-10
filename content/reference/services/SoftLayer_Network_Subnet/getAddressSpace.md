---
title: "getAddressSpace"
description: "The classifier of IP addresses this subnet represents, generally PUBLIC or PRIVATE. This does not necessarily correlate with the network on which the subnet is used."
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

### [REST Example](#getAddressSpace-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getAddressSpace-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Subnet/{SoftLayer_Network_SubnetID}/getAddressSpace'
```
