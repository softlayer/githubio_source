---
title: "createFromHardware"
description: "This method is used to create a new SoftLayer_Network_Storage_Allowed_Host using an existing SoftLayer_Hardware object's... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Allowed_Host_Subnet"
aliases:
    - "/reference/services/softlayer_network_storage_allowed_host_subnet/createFromHardware"
---
# [SoftLayer_Network_Storage_Allowed_Host_Subnet](/reference/services/SoftLayer_Network_Storage_Allowed_Host_Subnet)::createFromHardware

Creates and returns a new SoftLayer_Network_Storage_Allowed_Host.


## Overview 
This method is used to create a new SoftLayer_Network_Storage_Allowed_Host using an existing SoftLayer_Hardware object's id. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|hardwareId| integer| The ID of the SoftLayer_Hardware object to create a SoftLayer_Network_Storage_Allowed_Host object for.|
|iqn| string| The IQN to use when creating the SoftLayer_Network_Storage_Allowed_Host object, provide an empty string to have one generated automatically.|


### Required Headers
* authenticate

### Optional Headers
* SoftLayer_Network_Storage_Allowed_Host_SubnetObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Network_Storage_Allowed_Host_Subnet'>SoftLayer_Network_Storage_Allowed_Host_Subnet </a>

