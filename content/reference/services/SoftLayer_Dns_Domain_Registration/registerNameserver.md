---
title: "registerNameserver"
description: "The registerNameserver method creates a nameserver for the domain."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Dns"
classes:
    - "SoftLayer_Dns_Domain_Registration"
---
# SoftLayer_Dns_Domain_Registration::registerNameserver
## Overview 
The registerNameserver method creates a nameserver for the domain. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|nameserver| string| The fully qualified name of the nameserver|
|ipAddress| string| The IP Address of the nameserver|


### Required Headers
* authenticate
* SoftLayer_Dns_Domain_RegistrationInitParameters

### Optional Headers

### Return Values
boolean
