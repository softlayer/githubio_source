---
title: "removeSwipData"
description: "**DEPRECATED**
This function, when called on an instantiated SWIP transaction, will allow you to start a 'DELETE' transa... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Subnet_Swip_Transaction"
aliases:
    - "/reference/services/softlayer_network_subnet_swip_transaction/removeSwipData"
---
# [SoftLayer_Network_Subnet_Swip_Transaction](/reference/services/SoftLayer_Network_Subnet_Swip_Transaction)::removeSwipData

<div class="deprecated"><span class="deprecation-label">Deprecated </span></div>

Deletes registration information from ARIN for a single subnet


## Overview 

**DEPRECATED**
This function, when called on an instantiated SWIP transaction, will allow you to start a "DELETE" transaction with ARIN, allowing you to remove your SWIP registration information. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Network_Subnet_Swip_TransactionInitParameters


### Return Values
* boolean



### Error Handling

* SoftLayer_Exception_AccessDenied 

> Exception thrown if this method is attempted on a subnet not owned by the user. 

* SoftLayer_Exception_Network_Subnet_Swip_NotReadyForDelete 

> Exception thrown if this SWIP is not in OK status.  You cannot update a SWIP unless it is in OK status. 



