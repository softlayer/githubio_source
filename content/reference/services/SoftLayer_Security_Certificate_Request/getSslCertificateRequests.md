---
title: "getSslCertificateRequests"
description: "Returns all the SSL certificate requests. "
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

# [REST Example](#getSslCertificateRequests-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getSslCertificateRequests-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [int]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Security_Certificate_Request/getSslCertificateRequests'
```
