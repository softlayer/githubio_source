---
title: "getBandwidthImageByDate"
description: "Use this method when needing a bandwidth image for a single application delivery controller. It will gather the correct... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Application_Delivery_Controller"
aliases:
    - "/reference/services/softlayer_network_application_delivery_controller/getBandwidthImageByDate"
---
# [SoftLayer_Network_Application_Delivery_Controller](/reference/services/SoftLayer_Network_Application_Delivery_Controller)::getBandwidthImageByDate

Retrieve a visual representation of the amount of network traffic that occurred for the specified time frame for an application delivery controller. 


## Overview 
Use this method when needing a bandwidth image for a single application delivery controller. It will gather the correct input parameters for the generic graphing utility based on the date ranges 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|startDateTime| dateTime| datetime of the start date of the graph|
|endDateTime| dateTime| datetime of the ending date of the graph|
|networkType| string| $networkType   type of the graph, either "public" or "private"|


### Required Headers
* authenticate
* SoftLayer_Network_Application_Delivery_ControllerInitParameters

### Optional Headers

### Return Values
<a href='/reference/datatypes/SoftLayer_Container_Bandwidth_GraphOutputs'>SoftLayer_Container_Bandwidth_GraphOutputs </a>

