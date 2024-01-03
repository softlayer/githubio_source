---
title: "createNsRecord"
description: "Create an NS record on a SoftLayer domain. This is a shortcut method, meant to take the work out of creating a SoftLayer_Dns_Domain_ResourceRecord if you already have a domain record available. createNsRecord returns the newly created SoftLayer_Dns_Domain_ResourceRecord_NsType. "
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

# [REST Example](#createNsRecord-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#createNsRecord-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string, string, int]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Dns_Domain/{SoftLayer_Dns_DomainID}/createNsRecord'
```
