---
title: "autoComplete"
description: "This function is responsible for setting the Tags values. The internal flag is set to 0 if the user is a customer, and 1... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Tag"
classes:
    - "SoftLayer_Tag"
aliases:
    - "/reference/services/softlayer_tag/autoComplete"
---
# [SoftLayer_Tag](/reference/services/SoftLayer_Tag)::autoComplete


Autocomplete tag inputted by a user.


## Overview 
This function is responsible for setting the Tags values. The internal flag is set to 0 if the user is a customer, and 1 otherwise. AccountId is set to the account bound to the user, and the tags name is set to the clean version of the tag inputted by the user. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|tag| string| Tag inputted by the user.|


### Required Headers
* authenticate


### Optional Headers
* SoftLayer_TagObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Tag'>SoftLayer_Tag[] </a>




