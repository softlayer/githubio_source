---
title: "getAccount"
description: "The SoftLayer customer account that owns a domain."
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Dns"
classes:
    - "SoftLayer_Dns_Domain"
type: "reference"
layout: "method"
mainService : "SoftLayer_Dns_Domain"
---

### [REST Example](#getAccount-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getAccount-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Dns_Domain/{SoftLayer_Dns_DomainID}/getAccount'
```
