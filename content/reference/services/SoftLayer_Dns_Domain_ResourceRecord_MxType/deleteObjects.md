---
title: "deleteObjects"
description: "Remove multiple MX records from a domain. This follows the same logic as ''deleteObject'' and '''cannot be undone'''. The serial number of the domain associated with this MX record is updated upon deletion. 

''deleteObjects'' returns Boolean ''true'' on successful deletion or ''false'' if it was unable to remove a resource record. "
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

### [REST Example](#deleteObjects-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#deleteObjects-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Dns_Domain_ResourceRecord_MxType]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Dns_Domain_ResourceRecord_MxType/deleteObjects'
```
