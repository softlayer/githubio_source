---
title: "setVdrContent"
description: "This will update the bandwidth pool to the servers provided.  Servers currently in the bandwidth pool not provided on up... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Bandwidth_Version1_Allotment"
---
# SoftLayer_Network_Bandwidth_Version1_Allotment::setVdrContent
## Overview 
This will update the bandwidth pool to the servers provided.  Servers currently in the bandwidth pool not provided on update will be removed. Servers provided on update not currently in the bandwidth pool will be added. If all servers are removed, this removes the bandwidth pool on completion. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|hardware| <a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>| A collection of servers that will be used to set the bandwidth pool.|
|bareMetalServers| <a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>| A collection of bare metal servers that will be used to set the bandwidth pool.|
|virtualServerInstance| <a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest[] </a>| A collection of virtual server that will be used to set the bandwidth pool.|
|adc| <a href='/reference/datatypes/SoftLayer_Network_Application_Delivery_Controller'>SoftLayer_Network_Application_Delivery_Controller[] </a>| A collection of application delivery controllers that will be used to set the bandwidth pool.|
|optionalAllotmentId| integer| The bandwidth pool to move the servers to.  Provided only for backwards compatibility.|


### Required Headers
* authenticate
* SoftLayer_Network_Bandwidth_Version1_AllotmentInitParameters

### Optional Headers

### Return Values
boolean

