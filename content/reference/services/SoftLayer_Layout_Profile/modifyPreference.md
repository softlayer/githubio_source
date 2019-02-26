---
title: "modifyPreference"
description: "This method modifies an existing associated [[SoftLayer_Layout_Profile_Preference]] object. If the preference object bei... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Layout"
classes:
    - "SoftLayer_Layout_Profile"
aliases:
    - "/reference/services/softlayer_layout_profile/modifyPreference"
---
# [SoftLayer_Layout_Profile](/reference/services/SoftLayer_Layout_Profile)::modifyPreference

Modifies an associated layout preference


## Overview 
This method modifies an existing associated [[SoftLayer_Layout_Profile_Preference]] object. If the preference object being modified is a default value object, a new record is created to override the default value. 

Only preferences that are assigned to a profile may be updated. Attempts to update a non-existent preference object will result in an exception being thrown. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|templateObject| <a href='/reference/datatypes/SoftLayer_Layout_Profile_Preference'>SoftLayer_Layout_Profile_Preference </a>| |


### Required Headers
* authenticate
* SoftLayer_Layout_ProfileInitParameters


### Optional Headers
* SoftLayer_Layout_ProfileObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Layout_Profile_Preference'>SoftLayer_Layout_Profile_Preference </a>




