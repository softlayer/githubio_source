---
title: "getObject"
description: "getObject retrieves the SoftLayer_Software_VirtualLicense object whose ID number corresponds to the ID number of the ini... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Software"
classes:
    - "SoftLayer_Software_VirtualLicense"
aliases:
    - "/reference/services/softlayer_software_virtuallicense/getObject"
---
# [SoftLayer_Software_VirtualLicense](/reference/services/SoftLayer_Software_VirtualLicense)::getObject

Retrieve a SoftLayer_Software_VirtualLicense record.


## Overview 
getObject retrieves the SoftLayer_Software_VirtualLicense object whose ID number corresponds to the ID number of the init parameter passed to the SoftLayer_Software_VirtualLicense service. You can only retrieve Virtual Licenses assigned to your account number. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Software_VirtualLicenseInitParameters
* authenticate

### Optional Headers
* SoftLayer_Software_VirtualLicenseObjectMask
* SoftLayer_Software_VirtualLicenseObjectFilter
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Software_VirtualLicense'>SoftLayer_Software_VirtualLicense </a>

