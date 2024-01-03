---
title: "createObjects"
description: "Create multiple MX records on a domain. This follows the same logic as ''createObject'. The serial number of the domain associated with this MX record is updated upon creation. 

''createObjects'' returns Boolean ''true'' on successful creation or ''false'' if it was unable to create a resource record. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Dns"
classes:
    - "SoftLayer_Dns_Domain_ResourceRecord_MxType"
type: "reference"
layout: "method"
mainService : "SoftLayer_Dns_Domain_ResourceRecord_MxType"
---

# [REST Example](#createObjects-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#createObjects-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Dns_Domain_ResourceRecord]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Dns_Domain_ResourceRecord_MxType/createObjects'
```
