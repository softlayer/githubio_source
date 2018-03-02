---
title: "editObject"
description: "Account master users and sub-users who have the User Manage permission in the SoftLayer customer portal can update other... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer"
---
# SoftLayer_User_Customer::editObject
## Overview 
Account master users and sub-users who have the User Manage permission in the SoftLayer customer portal can update other user's information. Use editObject() if you wish to edit a single user account. Users who do not have the User Manage permission can only update their own information. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|templateObject| <a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer </a>| A skeleton SoftLayer_User_Customer object with only the properties defined that you wish to change. Unchanged properties are left alone.|


### Required Headers
* authenticate
* SoftLayer_User_CustomerInitParameters

### Optional Headers

### Return Values
boolean


### associatedMethods

*  [SoftLayer_User_Customer::editObjects](/reference/services/SoftLayer_User_Customer/editObjects )

