---
title: "requestVdrContentUpdates"
description: "This will move servers into a bandwidth pool, removing them from their previous bandwidth pool and optionally remove the... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Bandwidth_Version1_Allotment"
aliases:
    - "/reference/services/softlayer_network_bandwidth_version1_allotment/requestVdrContentUpdates"
---
# [SoftLayer_Network_Bandwidth_Version1_Allotment](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment)::requestVdrContentUpdates


Move servers into our out of a bandwidth pool.


## Overview 
This will move servers into a bandwidth pool, removing them from their previous bandwidth pool and optionally remove the bandwidth pool on completion. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|hardwareToAdd| <a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>| A collection of servers to be assigned to a bandwidth pool.|
|hardwareToRemove| <a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>| A collection of servers to be unassigned from an allotment and assigned to the virtual private rack|
|cloudsToAdd| <a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest[] </a>| A collection of virtual servers to be assigned to a bandwidth pool.|
|cloudsToRemove| <a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest[] </a>| A collection of virtual server to be unassigned from an allotment and assigned to the virtual private rack|
|optionalAllotmentId| integer| The bandwidth pool to move the servers to.  Provided only for backwards compatibility.|
|adcToAdd| <a href='/reference/datatypes/SoftLayer_Network_Application_Delivery_Controller'>SoftLayer_Network_Application_Delivery_Controller[] </a>| A collection of application delivery controllers to be assigned to a bandwidth pool.|
|adcToRemove| <a href='/reference/datatypes/SoftLayer_Network_Application_Delivery_Controller'>SoftLayer_Network_Application_Delivery_Controller[] </a>| A collection of application delivery controllers to be unassigned from an allotment and assigned to the virtual private rack|


### Required Headers
* authenticate
* SoftLayer_Network_Bandwidth_Version1_AllotmentInitParameters


### Return Values
* boolean



### Error Handling

* SoftLayer_Exception_NotFound 

> <<< EOT 

* SoftLayer_Exception_NotReady 

> <<< EOT 

* SoftLayer_Exception_NotSupported 

> <<< EOT 



