---
title: "resendSwipData"
description: "**DEPRECATED**
This function will allow you to update ARIN's registration data for a subnet to your current RWHOIS data."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Subnet_Swip_Transaction"
aliases:
    - "/reference/services/softlayer_network_subnet_swip_transaction/resendSwipData"
---
# [SoftLayer_Network_Subnet_Swip_Transaction](/reference/services/SoftLayer_Network_Subnet_Swip_Transaction)::resendSwipData

<div class="deprecated"><span class="deprecation-label">Deprecated </span></div>

Sends updated RWHOIS information to ARIN for a single subnet.


## Overview 

**DEPRECATED**
This function will allow you to update ARIN's registration data for a subnet to your current RWHOIS data. 

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

* SoftLayer_Exception_Network_Subnet_Swip_NotReadyForUpdate 

> Exception thrown if this SWIP is not in OK status.  You cannot update a SWIP unless it is in OK status. 



