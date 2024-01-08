---
title: "getAccount"
description: "The SoftLayer customer account that the domain is registered to."
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Dns"
classes:
    - "SoftLayer_Dns_Domain_Registration"
type: "reference"
layout: "method"
mainService : "SoftLayer_Dns_Domain_Registration"
---

### [REST Example](#getAccount-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getAccount-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Dns_Domain_Registration/{SoftLayer_Dns_Domain_RegistrationID}/getAccount'
```
