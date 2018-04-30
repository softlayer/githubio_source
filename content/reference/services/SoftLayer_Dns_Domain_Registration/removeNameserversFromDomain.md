---
title: "removeNameserversFromDomain"
description: "The removeNameserversFromDomain method removes nameservers from a domain for a domain that already has nameservers assig... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Dns"
classes:
    - "SoftLayer_Dns_Domain_Registration"
aliases:
    - "/reference/services/softlayer_dns_domain_registration/removeNameserversFromDomain"
---
# [SoftLayer_Dns_Domain_Registration](/reference/services/SoftLayer_Dns_Domain_Registration)::removeNameserversFromDomain

Removes nameservers from a domain.


## Overview 
The removeNameserversFromDomain method removes nameservers from a domain for a domain that already has nameservers assigned to it. 

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

