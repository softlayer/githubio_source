---
title: "deleteObjects"
description: "Like any other API object, the monitoring objects can be deleted by passing an instance of them into this function.  The... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Monitor_Version1_Query_Host"
aliases:
    - "/reference/services/softlayer_network_monitor_version1_query_host/deleteObjects"
---
# [SoftLayer_Network_Monitor_Version1_Query_Host](/reference/services/SoftLayer_Network_Monitor_Version1_Query_Host)::deleteObjects

Delete a group of Query_Host objects by passing in a collection of them


## Overview 
Like any other API object, the monitoring objects can be deleted by passing an instance of them into this function.  The ID on the object must be set. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|templateObjects| <a href='/reference/datatypes/SoftLayer_Network_Monitor_Version1_Query_Host'>SoftLayer_Network_Monitor_Version1_Query_Host[] </a>| An array of skeleton SoftLayer_Network_Monitor_Version1_Query_Host objects that you wish to delete. Each object in the array must have at least their id properties defined.|


### Required Headers
* authenticate

### Optional Headers

### Return Values
boolean

