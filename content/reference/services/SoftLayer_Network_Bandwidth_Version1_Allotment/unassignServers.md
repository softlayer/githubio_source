---
title: "unassignServers"
description: "This method will reassign a collection of SoftLayer hardware to the virtual private rack"
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Bandwidth_Version1_Allotment"
aliases:
    - "/reference/services/softlayer_network_bandwidth_version1_allotment/unassignServers"
---
# [SoftLayer_Network_Bandwidth_Version1_Allotment](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment)::unassignServers

unassign a collection of servers from an allotment and insert them into the accounts VPR.


## Overview 
This method will reassign a collection of SoftLayer hardware to the virtual private rack 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|templateObjects| <a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>| A collection of servers to be unassigned from an allotment and assigned to the virtual private rack|


### Required Headers
* authenticate

### Optional Headers

### Return Values
boolean

