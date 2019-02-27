---
title: "getObject"
description: "getObject retrieves the SoftLayer_Network_Bandwidth_Version1_Allotment object whose ID number corresponds to the ID numb... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Bandwidth_Version1_Allotment"
aliases:
    - "/reference/services/softlayer_network_bandwidth_version1_allotment/getObject"
---
# [SoftLayer_Network_Bandwidth_Version1_Allotment](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment)::getObject

Retrieve a SoftLayer_Network_Bandwidth_Version1_Allotment record.


## Overview 
getObject retrieves the SoftLayer_Network_Bandwidth_Version1_Allotment object whose ID number corresponds to the ID number of the init parameter passed to the SoftLayer_Hardware service. You can only retrieve an allotment associated with the account that your portal user is assigned to. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Network_Bandwidth_Version1_AllotmentInitParameters
* authenticate


### Optional Headers
* SoftLayer_Network_Bandwidth_Version1_AllotmentObjectMask
* SoftLayer_Network_Bandwidth_Version1_AllotmentObjectFilter
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Version1_Allotment'>SoftLayer_Network_Bandwidth_Version1_Allotment </a>



### Error Handling

* SoftLayer_Exception_ObjectNotFound 

> Throw the error "Unable to find object with id of {id}." if the given initialization parameter has an invalid id field. 

* SoftLayer_Exception_AccessDenied 

> Throw the error "Access Denied." if the given initialization parameter id field is not the account id of the user making the API call. 

* SoftLayer_Exception 

> Throw the error "Method has not been implemented for this object type." id the method is used. 

* SoftLayer_Exception 

> Throw the error "There is no virtual private rack for this account!" if an allotment that is being deleted still has servers associated with it. 

* SoftLayer_Exception 

> Throw the error "You must provide a new allotment ID." if a collection of servers are reassigned without providing an allotment id to assign them to. 

* SoftLayer_Exception 

> Throw the error "Invalid new allotment ID provided." if a collection of servers are reassigned to an allotment that doesnt exist. 

* SoftLayer_Exception 

> Throw the error "The account's virtual private rack can not be deleted." Softlayer accounts have a single virtual private rack(VPR) that all servers are assigned to by default.  The VPR can not be deleted. 



