---
title: "getLbaasListeners"
description: "Cloud Load Balancer [LBaaS] listeners currently associated with the certificate."
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

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Security_Certificate/{SoftLayer_Security_CertificateID}/getLbaasListeners'
```
