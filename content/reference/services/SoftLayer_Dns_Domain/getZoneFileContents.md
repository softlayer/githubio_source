---
title: "getZoneFileContents"
description: "Return a SoftLayer hosted domain and resource records' data formatted as zone file. "
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

### [REST Example](#getZoneFileContents-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getZoneFileContents-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Dns_Domain/{SoftLayer_Dns_DomainID}/getZoneFileContents'
```
