---
title: "editObjects"
description: "Edit multiple resource records on a domain. This follows the same logic as ''createObject'. The serial number of the domain associated with this resource record is updated upon creation. 

''createObjects'' returns Boolean ''true'' on successful creation or ''false'' if it was unable to create a resource record. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Dns"
classes:
    - "SoftLayer_Dns_Domain_ResourceRecord"
type: "reference"
layout: "method"
mainService : "SoftLayer_Dns_Domain_ResourceRecord"
---

### [REST Example](#editObjects-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#editObjects-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Dns_Domain_ResourceRecord]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Dns_Domain_ResourceRecord/editObjects'
```
