---
title: "requestVdrCancellation"
description: "This will remove a bandwidth pooling from a customer's allotments by cancelling the billing item.  All servers in that a... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Bandwidth_Version1_Allotment"
---
# SoftLayer_Network_Bandwidth_Version1_Allotment::requestVdrCancellation
## Overview 
This will remove a bandwidth pooling from a customer's allotments by cancelling the billing item.  All servers in that allotment will get moved to the account's vpr. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Network_Bandwidth_Version1_AllotmentInitParameters

### Optional Headers

### Return Values
boolean

