---
title: "getDiskSpaceUsageImageByDate"
description: "This method returns a disk usage graph wrapped in [[SoftLayer_Container_Bandwidth_GraphOutputsExtended|Bandwidth Graph]]... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_ContentDelivery_Account"
aliases:
    - "/reference/services/softlayer_network_contentdelivery_account/getDiskSpaceUsageImageByDate"
---
# [SoftLayer_Network_ContentDelivery_Account](/reference/services/SoftLayer_Network_ContentDelivery_Account)::getDiskSpaceUsageImageByDate

Returns an object with FTP disk usage graph data


## Overview 
This method returns a disk usage graph wrapped in [[SoftLayer_Container_Bandwidth_GraphOutputsExtended|Bandwidth Graph]] object. [[SoftLayer_Container_Bandwidth_GraphOutputsExtended|Bandwidth Graph]] object contains a starting time, ending time, graph title, graph binary data, and in and outbound total bytes. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|beginDateTime| dateTime| beginning time|
|endDateTime| dateTime| ending time|


### Required Headers
* authenticate
* SoftLayer_Network_ContentDelivery_AccountInitParameters


### Return Values
* <a href='/reference/datatypes/SoftLayer_Container_Bandwidth_GraphOutputs'>SoftLayer_Container_Bandwidth_GraphOutputs </a>


### Associated Methods

*  [SoftLayer_Network_ContentDelivery_Account::getDiskSpaceUsageDataByDate](/reference/services/SoftLayer_Network_ContentDelivery_Account/getDiskSpaceUsageDataByDate )



### Error Handling

* SoftLayer_Exception_Public 

> Throws an exception if a user does not have CDN_BANDWIDTH_VIEW privilege. 

* SoftLayer_Exception_Public 

> Throws an exception if the $beginDateTime is not a valid date value. 

* SoftLayer_Exception_Public 

> Throws an exception if the $endDateTime is not a valid date value. 



