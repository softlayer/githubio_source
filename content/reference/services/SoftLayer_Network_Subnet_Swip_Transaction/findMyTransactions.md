---
title: "findMyTransactions"
description: "**DEPRECATED**
This function will return an array of SoftLayer_Network_Subnet_Swip_Transaction objects, one for each SWI... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Subnet_Swip_Transaction"
aliases:
    - "/reference/services/softlayer_network_subnet_swip_transaction/findMyTransactions"
---
# [SoftLayer_Network_Subnet_Swip_Transaction](/reference/services/SoftLayer_Network_Subnet_Swip_Transaction)::findMyTransactions

returns SWIP transaction objects that are currently in transaction with ARIN.


## Overview 

**DEPRECATED**
This function will return an array of SoftLayer_Network_Subnet_Swip_Transaction objects, one for each SWIP that is currently in transaction with ARIN.  This includes all swip registrations, swip removal requests, and SWIP objects that are currently OK. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate


### Optional Headers
* SoftLayer_Network_Subnet_Swip_TransactionObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Network_Subnet_Swip_Transaction'>SoftLayer_Network_Subnet_Swip_Transaction[] </a>



### Error Handling

* SoftLayer_Exception_AccessDenied 

> Exception thrown if this method is attempted on a subnet not owned by the user. 



