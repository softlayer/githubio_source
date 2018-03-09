---
title: "updatePhone"
description: "Phone external binding supports a primary and a backup phone number. You can use this method to update your phone number... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_External_Binding_Phone"
---
# [SoftLayer_User_Customer_External_Binding_Phone](/reference/services/SoftLayer_User_Customer_External_Binding_Phone)::updatePhone

Updates the authentication phone numbers.


## Overview 
Phone external binding supports a primary and a backup phone number. You can use this method to update your phone number used for the phone authentication. You can provide an array of [[SoftLayer_Container_User_Data_Phone|User Phone]] objects. You have to mark one as the primary phone number by setting "phoneType" to "PRIMARY". 


*countryCode: Country code number for the phone number. Default: 1 (United States & Canada +1)
*phone: Phone number that 2 Form Factor system will call or text for user authentication.
The phone number format must match the format selected in the Country Code. 
*extension: Specify the extension that will be dialed after the call is answered. Digits, commas, *, and #
are allowed.  Commas can be used for a one second pause to navigate phone system menus. 
*phoneType: Specify the primary and backup phone number by setting this value to "PRIMARY" or "BACKUP".
If omitted, it will be considered to be the primary phone number. If you are passing two Phone objects, you must specify the phone type of each phone number. 



### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|phoneData| <a href='/reference/datatypes/SoftLayer_Container_User_Data_Phone'>SoftLayer_Container_User_Data_Phone[] </a>| |


### Required Headers
* authenticate
* SoftLayer_User_Customer_External_Binding_PhoneInitParameters

### Optional Headers

### Return Values
boolean

