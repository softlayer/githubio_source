---
title: "validateCsr"
description: "Allows you to validate a Certificate Signing Request (CSR) required for an SSL certificate with the certificate authorit... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Security"
classes:
    - "SoftLayer_Security_Certificate_Request"
aliases:
    - "/reference/services/softlayer_security_certificate_request/validateCsr"
---
# [SoftLayer_Security_Certificate_Request](/reference/services/SoftLayer_Security_Certificate_Request)::validateCsr

Validates a Certificate Signing Request (CSR) with the certificate authority (CA). 


## Overview 
Allows you to validate a Certificate Signing Request (CSR) required for an SSL certificate with the certificate authority (CA).  This method sends the CSR, the length of the subscription in months, the certificate type, and the server type for validation against requirements of the CA.  Returns true if valid. 

More information on CSR generation can be found at: [http://en.wikipedia.org/wiki/Certificate_signing_request Wikipedia] [https://knowledge.verisign.com/support/ssl-certificates-support/index?page=content&id=AR235&actp=LIST&viewlocale=en_US VeriSign] 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|csr| string| The encoded CSR data string.|
|validityMonths| integer| The length of the certificate subscription desired in months. Typically, 12 or 24 months.|
|itemId| integer| The product item identifier for the type of SSL certificate.|
|serverType| string| The type of server in which the certificate will be installed.|


### Required Headers
* authenticate


### Return Values
* boolean




