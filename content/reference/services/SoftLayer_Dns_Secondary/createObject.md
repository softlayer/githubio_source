---
title: "createObject"
description: "Create a secondary DNS record. The ''zoneName'', ''masterIpAddress'', and ''transferFrequency'' properties in the templa... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Dns"
classes:
    - "SoftLayer_Dns_Secondary"
---
# [SoftLayer_Dns_Secondary](/reference/services/SoftLayer_Dns_Secondary)::createObject

Create a secondary DNS record.


## Overview 
Create a secondary DNS record. The ''zoneName'', ''masterIpAddress'', and ''transferFrequency'' properties in the templateObject parameter are required parameters to create a secondary DNS record. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|templateObject| <a href='/reference/datatypes/SoftLayer_Dns_Secondary'>SoftLayer_Dns_Secondary </a>| The SoftLayer_Dns_Secondary object that you wish to create.|


### Required Headers
* authenticate

### Optional Headers
* SoftLayer_Dns_SecondaryObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Dns_Secondary'>SoftLayer_Dns_Secondary </a>


### associatedMethods

*  [SoftLayer_Dns_Secondary::createObjects](/reference/services/SoftLayer_Dns_Secondary/createObjects )

