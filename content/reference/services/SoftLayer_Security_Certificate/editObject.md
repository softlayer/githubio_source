---
title: "editObject"
description: "Update a certificate. Modifications are restricted to the note and CSR if the are any services associated with the certi... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Security"
classes:
    - "SoftLayer_Security_Certificate"
---
# [SoftLayer_Security_Certificate](/reference/services/SoftLayer_Security_Certificate)::editObject




## Overview 
Update a certificate. Modifications are restricted to the note and CSR if the are any services associated with the certificate. There are no modification restrictions for a certificate with no associated services. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|templateObject| <a href='/reference/datatypes/SoftLayer_Security_Certificate'>SoftLayer_Security_Certificate </a>| A skeleton SoftLayer_Security_Certificate object with only the properties defined that you wish to change. Unchanged properties are left alone.|


### Required Headers
* authenticate
* SoftLayer_Security_CertificateInitParameters

### Optional Headers

### Return Values
boolean

