---
title: "getResourceRecords"
description: "The individual records contained within a domain record. These include but are not limited to A, AAAA, MX, CTYPE, SPF and TXT records."
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

# [REST Example](#getResourceRecords-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getResourceRecords-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Dns_Domain/{SoftLayer_Dns_DomainID}/getResourceRecords'
```
