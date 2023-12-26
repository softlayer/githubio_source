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

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Dns_Secondary/{SoftLayer_Dns_SecondaryID}/transferNow'
```
