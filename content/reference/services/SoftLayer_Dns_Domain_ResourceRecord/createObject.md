---
title: "createObject"
description: "createObject creates a new domain resource record. The ''host'' property of the templateObject parameter is scrubbed to remove all non-alpha numeric characters except for '@', '_', '.', '*', and '-'. The ''data'' property of the templateObject parameter is scrubbed to remove all non-alphanumeric characters for '.' and '-'. Creating a resource record updates the serial number of the domain the resource record is associated with. 

''createObject'' returns Boolean ''true'' on successful create or ''false'' if it was unable to create a resource record. "
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

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Dns_Domain_ResourceRecord]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Dns_Domain_ResourceRecord/createObject'
```
