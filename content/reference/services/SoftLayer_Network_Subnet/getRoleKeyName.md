---
title: "getRoleKeyName"
description: "The role identifier that this subnet is participating in. Roles dictate how a subnet may be used."
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

### [REST Example](#getRoleKeyName-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getRoleKeyName-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Subnet/{SoftLayer_Network_SubnetID}/getRoleKeyName'
```
