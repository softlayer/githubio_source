---
title: "createObject"
description: "Add a certificate to your account for your records, or for use with various services. Only the certificate and private key are usually required. If your issuer provided an intermediate certificate, you must also provide that certificate. Details will be extracted from the certificate. Validation will be performed between the certificate and the private key as well as the certificate and the intermediate certificate, if provided. 

The certificate signing request is not required, but can be provided for your records. "
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
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Security_Certificate]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Security_Certificate/createObject'
```
