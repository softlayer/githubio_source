---
title: "editObject"
description: "Update a certificate. Modifications are restricted to the note and CSR if the are any services associated with the certificate. There are no modification restrictions for a certificate with no associated services. "
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

# [REST Example](#editObject-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#editObject-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Security_Certificate]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Security_Certificate/{SoftLayer_Security_CertificateID}/editObject'
```
