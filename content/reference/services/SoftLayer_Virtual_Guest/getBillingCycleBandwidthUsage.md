---
title: "getBillingCycleBandwidthUsage"
description: "Retrieve the raw bandwidth usage data for the current billing cycle. One object will be returned for each network this s... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Guest"
aliases:
    - "/reference/services/softlayer_virtual_guest/getBillingCycleBandwidthUsage"
---
# [SoftLayer_Virtual_Guest](/reference/services/SoftLayer_Virtual_Guest)::getBillingCycleBandwidthUsage


Retrieve the raw bandwidth usage data for the current billing cycle. One object will be returned for each network this server is attached to.


## Overview 
Retrieve the raw bandwidth usage data for the current billing cycle. One object will be returned for each network this server is attached to.

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Virtual_GuestInitParameters
* authenticate


### Optional Headers
* SoftLayer_Virtual_GuestObjectMask
* SoftLayer_Virtual_GuestObjectFilter
* resultLimit
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Usage'>SoftLayer_Network_Bandwidth_Usage[] </a>




