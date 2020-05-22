---
title: "modifyPreferences"
description: "Using this method, multiple [SoftLayer_Layout_Profile_Preference]({{<ref 'reference/datatypes/SoftLayer_Layout_Profile_P... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Layout"
classes:
    - "SoftLayer_Layout_Profile_Customer"
aliases:
    - "/reference/services/softlayer_layout_profile_customer/modifyPreferences"
---
# [SoftLayer_Layout_Profile_Customer](/reference/services/SoftLayer_Layout_Profile_Customer)::modifyPreferences

Modifies a collection of associated preferences


## Overview 
Using this method, multiple [SoftLayer_Layout_Profile_Preference]({{<ref "reference/datatypes/SoftLayer_Layout_Profile_Preference">}}) objects may be updated at once. 

Refer to [[SoftLayer_Layout_Profile::modifyPreference()]] for more information. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|layoutPreferenceObjects| <a href='/reference/datatypes/SoftLayer_Layout_Profile_Preference'>SoftLayer_Layout_Profile_Preference[] </a>| All the preferences to modify.|


### Required Headers
* authenticate
* SoftLayer_Layout_Profile_CustomerInitParameters


### Optional Headers
* SoftLayer_Layout_Profile_CustomerObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Layout_Profile_Preference'>SoftLayer_Layout_Profile_Preference[] </a>




