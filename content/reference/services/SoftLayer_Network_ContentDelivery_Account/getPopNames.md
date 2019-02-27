---
title: "getPopNames"
description: "This method returns an array of CDN POPs (Points of Presence) object. [[SoftLayer_Container_Network_ContentDelivery_Poin... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_ContentDelivery_Account"
aliases:
    - "/reference/services/softlayer_network_contentdelivery_account/getPopNames"
---
# [SoftLayer_Network_ContentDelivery_Account](/reference/services/SoftLayer_Network_ContentDelivery_Account)::getPopNames

Returns all CDN POPs (Points of Presence).


## Overview 
This method returns an array of CDN POPs (Points of Presence) object. [[SoftLayer_Container_Network_ContentDelivery_PointsOfPresence|POP object]] object contains the POP id and name. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Network_ContentDelivery_AccountInitParameters


### Return Values
* <a href='/reference/datatypes/SoftLayer_Container_Network_ContentDelivery_PointsOfPresence'>SoftLayer_Container_Network_ContentDelivery_PointsOfPresence[] </a>



### Error Handling

* SoftLayer_Exception_Public 

> Throws an exception if a user does not have CDN_BANDWIDTH_VIEW privilege. 



