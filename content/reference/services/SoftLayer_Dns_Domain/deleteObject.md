---
title: "deleteObject"
description: "deleteObject permanently removes a domain and all of it's associated resource records from the softlayer name servers. '''This cannot be undone.''' Be wary of running this method. If you remove a domain in error you will need to re-create it by creating a new SoftLayer_Dns_Domain object. "
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

### [REST Example](#deleteObject-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#deleteObject-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Dns_Domain/{SoftLayer_Dns_DomainID}/deleteObject'
```
