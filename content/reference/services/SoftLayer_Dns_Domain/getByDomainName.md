---
title: "getByDomainName"
description: "Search for [SoftLayer_Dns_Domain](/reference/datatypes/SoftLayer_Dns_Domain) records by domain name. getByDomainName() performs an inclusive search for domain records, returning multiple records based on partial name matches. Use this method to locate domain records if you don't have access to their id numbers. "
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

### [REST Example](#getByDomainName-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getByDomainName-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Dns_Domain/getByDomainName'
```
