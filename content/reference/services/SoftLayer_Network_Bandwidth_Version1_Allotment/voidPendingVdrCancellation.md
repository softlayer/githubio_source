---
title: "voidPendingVdrCancellation"
description: "This method will void a pending cancellation on a bandwidth pool. Note however any servers that belonged to the rack wil... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Bandwidth_Version1_Allotment"
aliases:
    - "/reference/services/softlayer_network_bandwidth_version1_allotment/voidPendingVdrCancellation"
---
# [SoftLayer_Network_Bandwidth_Version1_Allotment](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment)::voidPendingVdrCancellation


Void a pending cancellation on a bandwidth pool.


## Overview 
This method will void a pending cancellation on a bandwidth pool. Note however any servers that belonged to the rack will have to be restored individually using the method voidPendingServerMove($id, $type). 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Network_Bandwidth_Version1_AllotmentInitParameters


### Return Values
* boolean



### Error Handling

* SoftLayer_Exception_Public 

> Throw the exception "Permission denied." if the user calling the API does not have the "BANDWIDTH_MANAGE" permission. 

* SoftLayer_Exception_Public 

> Throw the exception "The current user does not have access to this allotment." if the user calling the API is trying to edit another account's virtual rack. 

* SoftLayer_Exception_Public 

> Throw the exception "The account's virtual private rack can not deleted." when calling this method on a virtual private rack. 

* SoftLayer_Exception_Public 

> Throw the exception "Your request has been cancelled because you are in your 12 hour billing window.  Please check back later." if your bandwidth pool is blocked for updates due to billing restrictions. 

* SoftLayer_Exception_Public 

> Throw the exception "Your request has been cancelled because there are currently bandwidth pooling transactions pending for this account.  Please check back later." if there is an active transaction currently running on the bandwidth pool. 

* SoftLayer_Exception_Public 

> Throw the exception "Unable to void pending cancellation.  Please contact support" if the API is unable to void the bandwidth pool cancellation. 



