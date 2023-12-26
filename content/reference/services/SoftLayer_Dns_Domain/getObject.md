---
title: "getObject"
description: "getObject retrieves the SoftLayer_Dns_Domain object whose ID number corresponds to the ID number of the init parameter passed to the SoftLayer_Dns_Domain service. You can only retrieve domains that are assigned to your SoftLayer account. "
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

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Dns_Domain/{SoftLayer_Dns_DomainID}/getObject'
```
