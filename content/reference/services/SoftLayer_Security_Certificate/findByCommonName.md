---
title: "findByCommonName"
description: "Locate certificates by their common name, traditionally a domain name."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Security"
classes:
    - "SoftLayer_Security_Certificate"
aliases:
    - "/reference/services/softlayer_security_certificate/findByCommonName"
---
# [SoftLayer_Security_Certificate](/reference/services/SoftLayer_Security_Certificate)::findByCommonName





## Overview 
Locate certificates by their common name, traditionally a domain name. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|commonName| string| the certificates common name|


### Required Headers
* authenticate


### Optional Headers
* SoftLayer_Security_CertificateObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Security_Certificate'>SoftLayer_Security_Certificate[] </a>




