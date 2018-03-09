---
title: "addNameserversToDomain"
description: "The addNameserversToDomain method adds nameservers to a domain for a domain that already has nameservers assigned to it.... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Dns"
classes:
    - "SoftLayer_Dns_Domain_Registration"
---
# [SoftLayer_Dns_Domain_Registration](/reference/services/SoftLayer_Dns_Domain_Registration)::addNameserversToDomain

Adds nameservers to a domain.


## Overview 
The addNameserversToDomain method adds nameservers to a domain for a domain that already has nameservers assigned to it. This method does not create a nameserver; the nameserver must already exist. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|nameservers| array of strings| Array of fully qualified name of the nameservers|


### Required Headers
* authenticate
* SoftLayer_Dns_Domain_RegistrationInitParameters

### Optional Headers

### Return Values
boolean

