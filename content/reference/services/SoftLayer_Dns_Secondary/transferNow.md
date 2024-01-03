---
title: "transferNow"
description: "Force a secondary DNS zone transfer by setting it's status 'Transfer Now'.  A zone transfer will be initiated within a minute of receiving this API call. "
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

# [REST Example](#transferNow-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#transferNow-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Dns_Secondary/{SoftLayer_Dns_SecondaryID}/transferNow'
```
