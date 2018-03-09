---
title: "getObject"
description: "getObject retrieves the SoftLayer_Network_Monitor_Version1_Query_Host object whose ID number corresponds to the ID numbe... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Monitor_Version1_Query_Host"
---
# [SoftLayer_Network_Monitor_Version1_Query_Host](/reference/services/SoftLayer_Network_Monitor_Version1_Query_Host)::getObject

Retrieve a SoftLayer_Network_Monitor_Version1_Query_Host record.


## Overview 
getObject retrieves the SoftLayer_Network_Monitor_Version1_Query_Host object whose ID number corresponds to the ID number of the init parameter passed to the SoftLayer_Network_Monitor_Version1_Query_Host service. You can only retrieve query hosts attached to hardware that belong to your account. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Network_Monitor_Version1_Query_HostInitParameters
* authenticate

### Optional Headers
* SoftLayer_Network_Monitor_Version1_Query_HostObjectMask
* SoftLayer_Network_Monitor_Version1_Query_HostObjectFilter
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Network_Monitor_Version1_Query_Host'>SoftLayer_Network_Monitor_Version1_Query_Host </a>

