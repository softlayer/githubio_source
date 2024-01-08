---
title: "deleteRegisteredNameserver"
description: "The deleteRegisteredNameserver method deletes a nameserver that was registered, provided it is not currently serving a domain "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Dns"
classes:
    - "SoftLayer_Dns_Domain_Registration"
type: "reference"
layout: "method"
mainService : "SoftLayer_Dns_Domain_Registration"
---

### [REST Example](#deleteRegisteredNameserver-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#deleteRegisteredNameserver-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Dns_Domain_Registration/{SoftLayer_Dns_Domain_RegistrationID}/deleteRegisteredNameserver'
```
