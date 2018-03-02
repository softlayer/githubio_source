---
title: "getRegionalInternetRegistryHandle"
description: "Retrieve the RIR handle that this registration object belongs to. This field may not be populated until the registration... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Subnet_Registration"
---
# SoftLayer_Network_Subnet_Registration::getRegionalInternetRegistryHandle
## Overview 
Retrieve the RIR handle that this registration object belongs to. This field may not be populated until the registration is complete.

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Network_Subnet_RegistrationInitParameters
* authenticate

### Optional Headers
* SoftLayer_Network_Subnet_RegistrationObjectMask
* SoftLayer_Network_Subnet_RegistrationObjectFilter
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Account_Rwhois_Handle'>SoftLayer_Account_Rwhois_Handle </a>

