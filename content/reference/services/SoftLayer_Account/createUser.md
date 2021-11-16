---
title: "createUser"
description: "Create a new Customer user record in the SoftLayer customer portal. This is a wrapper around the Customer::createObject... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account"
aliases:
    - "/reference/services/softlayer_account/createUser"
---
# [SoftLayer_Account](/reference/services/SoftLayer_Account)::createUser


Create a new user record, optionally skipping the IBMid email ("silently").


## Overview 
Create a new Customer user record in the SoftLayer customer portal. This is a wrapper around the Customer::createObject call, please see the documentation of that API. This wrapper adds the feature of the "silentlyCreate" option, which bypasses the IBMid invitation email process.  False (the default) goes through the IBMid invitation email process, which creates the IBMid/SoftLayer Single-Sign-On (SSO) user link when the invitation is accepted (meaning the email has been received, opened, and the link(s) inside the email have been clicked to complete the process). True will silently (no email) create the IBMid/SoftLayer user SSO link immediately. Either case will use the value in the template object 'email' field to indicate the IBMid to use. This can be the username or, if unique, the email address of an IBMid.  In the silent case, the IBMid must already exist.  In the non-silent invitation email case, the IBMid can be created during this flow, by specifying an email address to be used to create the IBMid.All the features and restrictions of createObject apply to this API as well.  In addition, note that the "silentlyCreate" flag is ONLY valid for IBMid-authenticated accounts. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|templateObject| <a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer </a>| as documented by createObject|
|password| string| as documented by createObject|
|vpnPassword| string| as documented by createObject|
|silentlyCreateFlag| boolean| - A flag to tell whether to go through the usual IBMid invitation email|


### Required Headers
* authenticate


### Optional Headers
* SoftLayer_AccountObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer </a>




