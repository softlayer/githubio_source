---
title: "getPemFormat"
description: "Retrieve the certificate in PEM (Privacy Enhanced Mail) format, which is a string containing all base64 encoded (DER) certificates delimited by -----BEGIN/END *----- clauses. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Security"
classes:
    - "SoftLayer_Security_Certificate"
type: "reference"
layout: "method"
mainService : "SoftLayer_Security_Certificate"
---

# [REST Example](#getPemFormat-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getPemFormat-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Security_Certificate/{SoftLayer_Security_CertificateID}/getPemFormat'
```
