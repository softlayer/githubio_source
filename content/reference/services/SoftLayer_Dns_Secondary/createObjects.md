---
title: "createObjects"
description: "Create multiple secondary DNS records. Each record passed to ''createObjects'' follows the logic in the SoftLayer_Dns_Se... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Dns"
classes:
    - "SoftLayer_Dns_Secondary"
---
# [SoftLayer_Dns_Secondary](/reference/services/SoftLayer_Dns_Secondary)::createObjects

Create multiple secondary DNS records.


## Overview 
Create multiple secondary DNS records. Each record passed to ''createObjects'' follows the logic in the SoftLayer_Dns_Secondary [[SoftLayer_Dns_Secondary::createObject|createObject]] method. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|templateObjects| <a href='/reference/datatypes/SoftLayer_Dns_Secondary'>SoftLayer_Dns_Secondary[] </a>| An array of SoftLayer_Dns_Secondary objects that you wish to create.|


### Required Headers
* authenticate

### Optional Headers
* SoftLayer_Dns_SecondaryObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Dns_Secondary'>SoftLayer_Dns_Secondary[] </a>


### associatedMethods

*  [SoftLayer_Dns_Secondary::createObject](/reference/services/SoftLayer_Dns_Secondary/createObject )

