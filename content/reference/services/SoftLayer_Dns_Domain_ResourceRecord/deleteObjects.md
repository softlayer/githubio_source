---
title: "deleteObjects"
description: "Remove multiple resource records from a domain. This follows the same logic as ''deleteObject'' and '''cannot be undone'''. The serial number of the domain associated with this resource record is updated upon deletion. You may not delete SOA records, PTR records, or NS resource records that point to ns1.softlayer.com or ns2.softlayer.com. 

''deleteObjects'' returns Boolean ''true'' on successful deletion or ''false'' if it was unable to remove a resource record. "
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

# [REST Example](#deleteObjects-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#deleteObjects-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Dns_Domain_ResourceRecord]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Dns_Domain_ResourceRecord/deleteObjects'
```
