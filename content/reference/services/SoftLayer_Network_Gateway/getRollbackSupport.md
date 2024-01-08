---
title: "getRollbackSupport"
description: "Returns the following statuses SUPPORTED - rollback is supported and perform automatically UNSUPPORTED - rollback is not supported MANUAL - rollback can be performed but 

"
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Gateway"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Gateway"
---

### [REST Example](#getRollbackSupport-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getRollbackSupport-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Gateway/{SoftLayer_Network_GatewayID}/getRollbackSupport'
```
