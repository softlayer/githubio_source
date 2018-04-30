---
title: "resendEmail"
description: "A Certificate Authority sends out various emails to your domain administrator or your technical contact. Use this servic... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Security"
classes:
    - "SoftLayer_Security_Certificate_Request"
aliases:
    - "/reference/services/softlayer_security_certificate_request/resendEmail"
---
# [SoftLayer_Security_Certificate_Request](/reference/services/SoftLayer_Security_Certificate_Request)::resendEmail

Have the Certificate Authority send various emails


## Overview 
A Certificate Authority sends out various emails to your domain administrator or your technical contact. Use this service to have these emails re-sent. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|emailType| string| Valid email types are: ApproverEmail, FulfillmentEmail|


### Required Headers
* authenticate
* SoftLayer_Security_Certificate_RequestInitParameters

### Optional Headers

### Return Values
boolean

