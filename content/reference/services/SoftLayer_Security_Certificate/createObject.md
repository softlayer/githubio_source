---
title: "createObject"
description: "Add a certificate to your account for your records, or for use with various services. Only the certificate and private k... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Security"
classes:
    - "SoftLayer_Security_Certificate"
---
# [SoftLayer_Security_Certificate](/reference/services/SoftLayer_Security_Certificate)::createObject




## Overview 
Add a certificate to your account for your records, or for use with various services. Only the certificate and private key are usually required. If your issuer provided an intermediate certificate, you must also provide that certificate. Details will be extracted from the certificate. Validation will be performed between the certificate and the private key as well as the certificate and the intermediate certificate, if provided. 

The certificate signing request is not required, but can be provided for your records. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|templateObject| <a href='/reference/datatypes/SoftLayer_Security_Certificate'>SoftLayer_Security_Certificate </a>| The SoftLayer_Security_Certificate object that you wish to create.|


### Required Headers
* authenticate

### Optional Headers
* SoftLayer_Security_CertificateObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Security_Certificate'>SoftLayer_Security_Certificate </a>

