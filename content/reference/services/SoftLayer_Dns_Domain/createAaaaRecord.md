---
title: "createAaaaRecord"
description: "Create an AAAA record on a SoftLayer domain. This is a shortcut method, meant to take the work out of creating a SoftLayer_Dns_Domain_ResourceRecord if you already have a domain record available. createARecord returns the newly created SoftLayer_Dns_Domain_ResourceRecord_AaaaType. "
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

# [REST Example](#createAaaaRecord-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#createAaaaRecord-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string, string, int]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Dns_Domain/{SoftLayer_Dns_DomainID}/createAaaaRecord'
```
