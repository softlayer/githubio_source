---
title: "editObject"
description: "The password and/or notes may be modified.  Modifying the EVault passwords here will also update the password the Webcc... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account_Password"
aliases:
    - "/reference/services/softlayer_account_password/editObject"
---
# [SoftLayer_Account_Password](/reference/services/SoftLayer_Account_Password)::editObject

Edit the password and/or notes for an account password.


## Overview 
The password and/or notes may be modified.  Modifying the EVault passwords here will also update the password the Webcc interface will use. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|templateObject| <a href='/reference/datatypes/SoftLayer_Account_Password'>SoftLayer_Account_Password </a>| A skeleton SoftLayer_Account_Password object with only the properties defined that you wish to change. Unchanged properties are left alone.|


### Required Headers
* authenticate
* SoftLayer_Account_PasswordInitParameters

### Optional Headers

### Return Values
boolean

