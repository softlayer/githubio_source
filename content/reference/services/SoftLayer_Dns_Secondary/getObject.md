---
title: "getObject"
description: "getObject retrieves the SoftLayer_Dns_Secondary object whose ID number corresponds to the ID number of the init paramater passed to the SoftLayer_Dns_Secondary service. You can only retrieve a secondary DNS record that is assigned to your SoftLayer customer account. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Dns"
classes:
    - "SoftLayer_Dns_Secondary"
type: "reference"
layout: "method"
mainService : "SoftLayer_Dns_Secondary"
---

# [REST Example](#getObject-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getObject-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Dns_Secondary/{SoftLayer_Dns_SecondaryID}/getObject'
```
