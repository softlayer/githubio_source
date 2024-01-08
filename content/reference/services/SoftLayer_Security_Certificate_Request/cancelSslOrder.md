---
title: "cancelSslOrder"
description: "Cancels a pending SSL certificate order at the Certificate Authority "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Security"
classes:
    - "SoftLayer_Security_Certificate_Request"
type: "reference"
layout: "method"
mainService : "SoftLayer_Security_Certificate_Request"
---

### [REST Example](#cancelSslOrder-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#cancelSslOrder-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Security_Certificate_Request/{SoftLayer_Security_Certificate_RequestID}/cancelSslOrder'
```
