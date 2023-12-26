---
title: "getByDomainName"
description: "Search for [SoftLayer_Dns_Secondary](/reference/datatypes/SoftLayer_Dns_Secondary) records by domain name. getByDomainName() performs an inclusive search for secondary domain records, returning multiple records based on partial name matches. Use this method to locate secondary domain records if you don't have access to their id numbers. "
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
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Dns_Secondary/getByDomainName'
```
