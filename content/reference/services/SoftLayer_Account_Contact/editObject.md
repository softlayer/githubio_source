---
title: "editObject"
description: "This method allows you to modify an account contact. Only master users are permitted to modify an account contact."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account_Contact"
aliases:
    - "/reference/services/softlayer_account_contact/editObject"
---
# [SoftLayer_Account_Contact](/reference/services/SoftLayer_Account_Contact)::editObject


Edit an existing account contact.


## Overview 
This method allows you to modify an account contact. Only master users are permitted to modify an account contact. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|templateObject| <a href='/reference/datatypes/SoftLayer_Account_Contact'>SoftLayer_Account_Contact </a>| A skeleton SoftLayer_Account_Contact object with only the properties defined that you wish to change. Unchanged properties are left alone.|


### Required Headers
* authenticate
* SoftLayer_Account_ContactInitParameters


### Return Values
* boolean



### Error Handling

* SoftLayer_Exception_Public 

> Throw the error 'Only the master user for an account may modify account contact information.' if a user other than the master user attempts to modify an account contact. 



