---
title: "createObjects"
description: "Passing in a collection of unsaved instances of Query_Host objects into this function will create all objects and return... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Monitor_Version1_Query_Host"
aliases:
    - "/reference/services/softlayer_network_monitor_version1_query_host/createObjects"
---
# [SoftLayer_Network_Monitor_Version1_Query_Host](/reference/services/SoftLayer_Network_Monitor_Version1_Query_Host)::createObjects

Create multiple monitoring entries at once


## Overview 
Passing in a collection of unsaved instances of Query_Host objects into this function will create all objects and return the results to the user. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|templateObjects| <a href='/reference/datatypes/SoftLayer_Network_Monitor_Version1_Query_Host'>SoftLayer_Network_Monitor_Version1_Query_Host[] </a>| An array of SoftLayer_Network_Monitor_Version1_Query_Host objects that you wish to create.|


### Required Headers
* authenticate


### Optional Headers
* SoftLayer_Network_Monitor_Version1_Query_HostObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Network_Monitor_Version1_Query_Host'>SoftLayer_Network_Monitor_Version1_Query_Host[] </a>




