---
title: "voidPendingServerMove"
description: "This method will void a pending server removal from this bandwidth pooling. Pass in the id of the hardware object or vir... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Bandwidth_Version1_Allotment"
aliases:
    - "/reference/services/softlayer_network_bandwidth_version1_allotment/voidPendingServerMove"
---
# [SoftLayer_Network_Bandwidth_Version1_Allotment](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment)::voidPendingServerMove


Void a pending server removal from this bandwidth pooling.


## Overview 
This method will void a pending server removal from this bandwidth pooling. Pass in the id of the hardware object or virtual guest you wish to update. Assuming that object is currently pending removal from the bandwidth pool at the start of the next billing cycle, the bandwidth pool member status will be restored and the pending cancellation removed. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|id| integer| The id number of the server or computing instance you wish to void moving to a virtual rack.|
|type| string| The string "SoftLayer_Hardware" or "SoftLayer_Virtual_Guest" depending on the what you were moving to a virtual rack.|


### Required Headers
* authenticate
* SoftLayer_Network_Bandwidth_Version1_AllotmentInitParameters


### Return Values
* boolean



### Error Handling

* SoftLayer_Exception_Public 

> Throw the exception "Permission denied." if the user calling the API does not have the "BANDWIDTH_MANAGE" permission. 

* SoftLayer_Exception_Public 

> Throw the exception "The current user does not have access to this allotment." is the user calling the API is trying to edit another account's bandwidth pooling. 

* SoftLayer_Exception_Public 

> Throw the exception "Your request has been cancelled because you are in 12 hour billing window.  Please check back later." if your dandwidth pool is blocked from updates for billing reasons. 

* SoftLayer_Exception_Public 

> Throw the exception "Your request has been cancelled because there are currently bandwidth pooling transactions pending for this account.  Please check back later." if your bandwidth pool rack is currently processing a transaction. 

* SoftLayer_Exception_Public 

> Throw the exception "Invalid type parameter." if the type parameter is a string other than "SoftLayer_Hardware" or "SoftLayer_Virtual_Guest". 

* SoftLayer_Exception_Public 

> Throw the exception "You cannot void the pending server move while the allotment is still pending cancellation." if your bandwidth pool has an end date set. 

* SoftLayer_Exception_Public 

> Throw the exception "The current user does not own this server or virtual guest." if the user calling the API does not have access to the server or virtual server passed to this method. 

* SoftLayer_Exception_Public 

> Throw the exception "Unable to void pending cancellation.  Please contact support" if the API is unable to void a pending server move. 



