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

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|id| integer| The id number of the server or computing instance you wish to void moving to a virtual rack.|
|type| string| The string "SoftLayer_Hardware" or "SoftLayer_Virtual_Guest" depending on the what you were moving to a virtual rack.|


### Required Headers
* authenticate
* SoftLayer_Network_Bandwidth_Version1_AllotmentInitParameters

### Optional Headers

### Return Values
boolean

