---
title: "findMyTransactions"
description: "This function will return an array of SoftLayer_Network_Subnet_Swip_Transaction objects, one for each SWIP that is curre... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Subnet_Swip_Transaction"
---
# SoftLayer_Network_Subnet_Swip_Transaction::findMyTransactions
## Overview 
This function will return an array of SoftLayer_Network_Subnet_Swip_Transaction objects, one for each SWIP that is currently in transaction with ARIN.  This includes all swip registrations, swip removal requests, and SWIP objects that are currently OK. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate

### Optional Headers
* SoftLayer_Network_Subnet_Swip_TransactionObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Network_Subnet_Swip_Transaction'>SoftLayer_Network_Subnet_Swip_Transaction[] </a>
