---
title: "deleteObject"
description: "Delete a secondary DNS Record. This will also remove any associated domain records and resource records on the SoftLayer nameservers that were created as a result of the zone transfers. This action cannot be undone. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Dns"
classes:
    - "SoftLayer_Dns_Secondary"
type: "reference"
layout: "method"
mainService : "SoftLayer_Dns_Secondary"
---

# [REST Example](#deleteObject-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#deleteObject-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Dns_Secondary/{SoftLayer_Dns_SecondaryID}/deleteObject'
```
