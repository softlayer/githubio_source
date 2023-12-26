---
title: "editObject"
description: "editObject edits an existing MX resource record. The ''host'' property of the templateObject parameter is scrubbed to remove all non-alpha numeric characters except for '@', '_', '.', '*', and '-'. The ''data'' property of the templateObject parameter is scrubbed to remove all non-alphanumeric characters for '.' and '-'. Editing an MX record updates the serial number of the domain the record is associated with. 

''editObject'' returns Boolean ''true'' on a successful edit or ''false'' if it was unable to edit the resource record. "
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

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Dns_Domain_ResourceRecord_MxType]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Dns_Domain_ResourceRecord_MxType/{SoftLayer_Dns_Domain_ResourceRecord_MxTypeID}/editObject'
```
