---
title: "changePreference"
description: "Select a type of preference you would like to modify using [SoftLayer_User_Customer::getPreferenceTypes]({{<ref 'referen... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_OpenIdConnect_TrustedProfile"
aliases:
    - "/reference/services/softlayer_user_customer_openidconnect_trustedprofile/changePreference"
---
# [SoftLayer_User_Customer_OpenIdConnect_TrustedProfile](/reference/services/SoftLayer_User_Customer_OpenIdConnect_TrustedProfile)::changePreference


Change preference values for the current user


## Overview 
Select a type of preference you would like to modify using [SoftLayer_User_Customer::getPreferenceTypes]({{<ref "reference/services/SoftLayer_User_Customer/getPreferenceTypes">}}) and invoke this method using that preference type key name. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|preferenceTypeKeyName| string| A valid preference type key name from SoftLayer_User_Preference_Type|
|value| string| Any valid value for the preference type|


### Required Headers
* authenticate
* SoftLayer_User_Customer_OpenIdConnect_TrustedProfileInitParameters


### Optional Headers
* SoftLayer_User_Customer_OpenIdConnect_TrustedProfileObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_User_Preference'>SoftLayer_User_Preference[] </a>




