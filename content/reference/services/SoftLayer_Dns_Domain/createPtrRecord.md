---
title: "createPtrRecord"
description: "setPtrRecordForIpAddress() sets a single reverse DNS record for a single IP address and returns the newly created or edited [SoftLayer_Dns_Domain_ResourceRecord](/reference/datatypes/SoftLayer_Dns_Domain_ResourceRecord) record. Currently this method only supports IPv4 addresses and performs no operation when given an IPv6 address. "
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

### [REST Example](#createPtrRecord-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#createPtrRecord-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string, string, int]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Dns_Domain/createPtrRecord'
```
