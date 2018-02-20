---
title: "sendRegistrantVerificationEmail"
description: "When a domain is registered or transferred, or when the registrant contact information is changed, the registrant must r... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Dns"
classes:
    - "SoftLayer_Dns_Domain_Registration"
---
# SoftLayer_Dns_Domain_Registration::sendRegistrantVerificationEmail
## Overview 
When a domain is registered or transferred, or when the registrant contact information is changed, the registrant must reply to an email requesting them to confirm that the submitted contact information is correct. This method sends the verification email to the registrant. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Dns_Domain_RegistrationInitParameters

### Optional Headers

### Return Values
boolean
