---
title: "validateCsr"
description: "Allows you to validate a Certificate Signing Request (CSR) required for an SSL certificate with the certificate authority (CA).  This method sends the CSR, the length of the subscription in months, the certificate type, and the server type for validation against requirements of the CA.  Returns true if valid. 

More information on CSR generation can be found at: [http://en.wikipedia.org/wiki/Certificate_signing_request Wikipedia] [https://www.digicert.com/csr-creation.htm DigiCert] "
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

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string, int, int, string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Security_Certificate_Request/validateCsr'
```
