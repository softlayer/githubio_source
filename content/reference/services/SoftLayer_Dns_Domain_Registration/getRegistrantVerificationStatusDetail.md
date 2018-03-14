---
title: "getRegistrantVerificationStatusDetail"
description: "When a domain is registered or transferred, or when the registrant contact information is changed, the registrant must r... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Dns"
classes:
    - "SoftLayer_Dns_Domain_Registration"
aliases:
    - "/reference/services/softlayer_dns_domain_registration/getRegistrantVerificationStatusDetail"
---
# [SoftLayer_Dns_Domain_Registration](/reference/services/SoftLayer_Dns_Domain_Registration)::getRegistrantVerificationStatusDetail

Retrieves registrant verification status.


## Overview 
When a domain is registered or transferred, or when the registrant contact information is changed, the registrant must reply to an email requesting them to confirm that the submitted contact information is correct. This method returns the current state of the verification request. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Dns_Domain_RegistrationInitParameters

### Optional Headers

### Return Values
<a href='/reference/datatypes/SoftLayer_Container_Dns_Domain_Registration_Registrant_Verification_StatusDetail'>SoftLayer_Container_Dns_Domain_Registration_Registrant_Verification_StatusDetail </a>

