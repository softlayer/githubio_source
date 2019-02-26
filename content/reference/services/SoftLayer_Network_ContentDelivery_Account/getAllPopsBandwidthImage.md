---
title: "getAllPopsBandwidthImage"
description: "This method returns a bandwidth graph for every POP wrapped in [[SoftLayer_Container_Bandwidth_GraphOutputsExtended|Band... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_ContentDelivery_Account"
aliases:
    - "/reference/services/softlayer_network_contentdelivery_account/getAllPopsBandwidthImage"
---
# [SoftLayer_Network_ContentDelivery_Account](/reference/services/SoftLayer_Network_ContentDelivery_Account)::getAllPopsBandwidthImage

Returns an object with bandwidth graph data for each POP


## Overview 
This method returns a bandwidth graph for every POP wrapped in [[SoftLayer_Container_Bandwidth_GraphOutputsExtended|Bandwidth Graph]] object. A POP bandwidth graph shows bandwidth consumption per each POP in a bar graph. [[SoftLayer_Container_Bandwidth_GraphOutputsExtended|Bandwidth Graph]] object contains a begin time, end time, title of the graph, binary date, in and outbound total bandwidth in bytes 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|title| string| Title of the bandwidth graph|
|beginDateTime| dateTime| The beginning time|
|endDateTime| dateTime| ending time|
|unit| string| The bandwidth unit. B (byte), MB (megabyte) and GB (gigabyte) are supported|


### Required Headers
* authenticate
* SoftLayer_Network_ContentDelivery_AccountInitParameters


### Return Values
* <a href='/reference/datatypes/SoftLayer_Container_Bandwidth_GraphOutputsExtended'>SoftLayer_Container_Bandwidth_GraphOutputsExtended </a>


### Associated Methods

*  [SoftLayer_Network_ContentDelivery_Account::getBandwidthData](/reference/services/SoftLayer_Network_ContentDelivery_Account/getBandwidthData )
*  [SoftLayer_Network_ContentDelivery_Account::getAllPopsBandwidthData](/reference/services/SoftLayer_Network_ContentDelivery_Account/getAllPopsBandwidthData )



### Error Handling

* SoftLayer_Exception_Public 

> Throws an exception if a user does not have CDN_BANDWIDTH_VIEW privilege. 

* SoftLayer_Exception_Public 

> Throws an exception if the $beginDateTime is not a valid date value. 

* SoftLayer_Exception_Public 

> Throws an exception if the $endDateTime is not a valid date value. 

* SoftLayer_Exception_Public 

> Throws an exception if an invalid $unit is passed.  B, MB and GB are supported. 



