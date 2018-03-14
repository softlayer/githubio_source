---
title: "getBandwidthImage"
description: "This method returns a bandwidth graph wrapped in [[SoftLayer_Container_Bandwidth_GraphOutputsExtended|Bandwidth Graph]]... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_ContentDelivery_Account"
aliases:
    - "/reference/services/softlayer_network_contentdelivery_account/getBandwidthImage"
---
# [SoftLayer_Network_ContentDelivery_Account](/reference/services/SoftLayer_Network_ContentDelivery_Account)::getBandwidthImage

Returns an object with bandwidth graph data


## Overview 
This method returns a bandwidth graph wrapped in [[SoftLayer_Container_Bandwidth_GraphOutputsExtended|Bandwidth Graph]] object. [[SoftLayer_Container_Bandwidth_GraphOutputsExtended|Bandwidth Graph]] object contains a starting time, ending time, graph title, graph binary data, and in and outbound total bytes. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|title| string| of the bandwidth graph|
|beginDateTime| dateTime| beginning time|
|endDateTime| dateTime| ending time|


### Required Headers
* authenticate
* SoftLayer_Network_ContentDelivery_AccountInitParameters

### Optional Headers

### Return Values
<a href='/reference/datatypes/SoftLayer_Container_Bandwidth_GraphOutputsExtended'>SoftLayer_Container_Bandwidth_GraphOutputsExtended </a>


### associatedMethods

*  [SoftLayer_Network_ContentDelivery_Account::getBandwidthData](/reference/services/SoftLayer_Network_ContentDelivery_Account/getBandwidthData )

