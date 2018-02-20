---
title: "deleteRegisteredNameserver"
description: "The deleteRegisteredNameserver method deletes a nameserver that was registered, provided it is not currently serving a d... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Dns"
classes:
    - "SoftLayer_Dns_Domain_Registration"
---
# SoftLayer_Dns_Domain_Registration::deleteRegisteredNameserver
## Overview 
The deleteRegisteredNameserver method deletes a nameserver that was registered, provided it is not currently serving a domain 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|nameserver| string| The fully qualified name of the nameserver|


### Required Headers
* authenticate
* SoftLayer_Dns_Domain_RegistrationInitParameters

### Optional Headers

### Return Values
boolean
