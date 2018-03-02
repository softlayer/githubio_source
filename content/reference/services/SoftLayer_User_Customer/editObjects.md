---
title: "editObjects"
description: "Account master users and sub-users who have the User Manage permission in the SoftLayer customer portal can update other... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer"
---
# SoftLayer_User_Customer::editObjects
## Overview 
Account master users and sub-users who have the User Manage permission in the SoftLayer customer portal can update other user's information. Use editObjects() if you wish to edit multiple users at once. Users who do not have the User Manage permission can only update their own information. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|templateObjects| <a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer[] </a>| An array of skeleton SoftLayer_User_Customer objects with only the properties defined that you wish to change. Unchanged properties are left alone.|


### Required Headers
* authenticate

### Optional Headers

### Return Values
boolean


### associatedMethods

*  [SoftLayer_User_Customer::editObject](/reference/services/SoftLayer_User_Customer/editObject )

