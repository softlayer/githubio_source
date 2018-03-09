---
title: "verifyDomainMapping"
description: "Verifies the status of the domain mapping by calling the rest api; will update the status, cname, and vendorCName if nec... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_CdnMarketplace_Configuration_Mapping"
---
# [SoftLayer_Network_CdnMarketplace_Configuration_Mapping](/reference/services/SoftLayer_Network_CdnMarketplace_Configuration_Mapping)::verifyDomainMapping

This method will verify the status of a domain mapping 


## Overview 
Verifies the status of the domain mapping by calling the rest api; will update the status, cname, and vendorCName if necessary and will return the updated values. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|uniqueId| integer| |


### Required Headers
* authenticate

### Optional Headers

### Return Values
<a href='/reference/datatypes/SoftLayer_Container_Network_CdnMarketplace_Configuration_Mapping'>SoftLayer_Container_Network_CdnMarketplace_Configuration_Mapping[] </a>

