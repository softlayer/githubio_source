---
title: "modifyRegisteredNameserver"
description: "The modifyRegisteredNameserver method modifies a nameserver that was registered."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Dns"
classes:
    - "SoftLayer_Dns_Domain_Registration"
---
# SoftLayer_Dns_Domain_Registration::modifyRegisteredNameserver
## Overview 
The modifyRegisteredNameserver method modifies a nameserver that was registered. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|oldNameserver| string| The old, fully qualified domain name of the nameserver|
|newNameserver| string| The new, fully qualified domain name for the nameserver|
|ipAddress| string| The IP Address of the nameserver|


### Required Headers
* authenticate
* SoftLayer_Dns_Domain_RegistrationInitParameters

### Optional Headers

### Return Values
boolean

