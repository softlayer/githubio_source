---
title: "getLargestAllowedSubnetCidr"
description: "Computes the number of available public secondary IP addresses, aligned to a subnet size."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account"
aliases:
    - "/reference/services/softlayer_account/getLargestAllowedSubnetCidr"
---
# [SoftLayer_Account](/reference/services/SoftLayer_Account)::getLargestAllowedSubnetCidr

Computes the number of available public secondary IP addresses, augmented by the provided number of hosts, before overflow of the allowed host to IP address ratio occurs. The result is aligned to the nearest subnet size that could be accommodated in full. 

0 is returned if an overflow is detected. 

The use of $locationId has been deprecated. 


## Overview 
Computes the number of available public secondary IP addresses, aligned to a subnet size. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|numberOfHosts| integer| Number of hosts to adjust the current server count by|
|locationId| integer| Deprecated|


### Required Headers
* authenticate


### Return Values
* integer




