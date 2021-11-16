---
title: "getAttachedTagsForCurrentUser"
description: "Get all tags with at least one reference attached to it for the current account. The total items header for this method... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Tag"
classes:
    - "SoftLayer_Tag"
aliases:
    - "/reference/services/softlayer_tag/getAttachedTagsForCurrentUser"
---
# [SoftLayer_Tag](/reference/services/SoftLayer_Tag)::getAttachedTagsForCurrentUser


Get the tags attached to references.


## Overview 
Get all tags with at least one reference attached to it for the current account. The total items header for this method contains the total number of attached tags even if a result limit is applied. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate


### Optional Headers
* SoftLayer_TagObjectMask
* SoftLayer_ObjectMask
* resultLimit

### Return Values
* <a href='/reference/datatypes/SoftLayer_Tag'>SoftLayer_Tag[] </a>




