---
title: "getNetworkComponentFirewall"
description: "The hardware firewall associated to this subnet via access control list."
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

### [REST Example](#getNetworkComponentFirewall-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getNetworkComponentFirewall-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Subnet/{SoftLayer_Network_SubnetID}/getNetworkComponentFirewall'
```
