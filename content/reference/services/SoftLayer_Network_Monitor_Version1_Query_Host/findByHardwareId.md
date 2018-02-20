---
title: "findByHardwareId"
description: "This method returns all Query_Host objects associated with the passed in hardware ID as long as that hardware ID is owne... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Monitor_Version1_Query_Host"
---
# SoftLayer_Network_Monitor_Version1_Query_Host::findByHardwareId
## Overview 
This method returns all Query_Host objects associated with the passed in hardware ID as long as that hardware ID is owned by the current user's account. 

This behavior can also be accomplished by simply tapping networkMonitors on the Hardware_Server object. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|hardwareId| integer| The ID of the hardware to search by.|


### Required Headers
* authenticate

### Optional Headers
* SoftLayer_Network_Monitor_Version1_Query_HostObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Network_Monitor_Version1_Query_Host'>SoftLayer_Network_Monitor_Version1_Query_Host[] </a>
