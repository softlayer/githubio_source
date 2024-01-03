---
title: "editObject"
description: "This method will edit an existing SoftLayer_Network_Subnet_Registration object. For more detail, see [SoftLayer_Network_Subnet_Registration::createObject](/reference/datatypes/$1/#$2). "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Subnet_Registration"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Subnet_Registration"
---

# [REST Example](#editObject-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#editObject-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Network_Subnet_Registration]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Subnet_Registration/{SoftLayer_Network_Subnet_RegistrationID}/editObject'
```
