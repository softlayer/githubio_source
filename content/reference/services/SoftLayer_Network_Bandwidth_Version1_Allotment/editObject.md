---
title: "editObject"
description: "Edit a bandwidth allotment's local properties. Currently you may only change an allotment's name. Use the [[SoftLayer_Ne... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Bandwidth_Version1_Allotment"
aliases:
    - "/reference/services/softlayer_network_bandwidth_version1_allotment/editObject"
---
# [SoftLayer_Network_Bandwidth_Version1_Allotment](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment)::editObject

Edit a bandwidth allotment


## Overview 
Edit a bandwidth allotment's local properties. Currently you may only change an allotment's name. Use the [[SoftLayer_Network_Bandwidth_Version1_Allotment::reassignServers|reassignServers()]] and [[SoftLayer_Network_Bandwidth_Version1_Allotment::unassignServers|unassignServers()]] methods to move servers in and out of your allotments. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|templateObject| <a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Version1_Allotment'>SoftLayer_Network_Bandwidth_Version1_Allotment </a>| A skeleton SoftLayer_Network_Bandwidth_Version1_Allotment object with only the properties defined that you wish to change. Unchanged properties are left alone.|


### Required Headers
* authenticate
* SoftLayer_Network_Bandwidth_Version1_AllotmentInitParameters


### Return Values
* boolean




