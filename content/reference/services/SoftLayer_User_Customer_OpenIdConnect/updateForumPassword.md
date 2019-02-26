---
title: "updateForumPassword"
description: "This method is deprecated! SoftLayer Community Forums no longer exist, therefore, this method will return false. In the... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_OpenIdConnect"
aliases:
    - "/reference/services/softlayer_user_customer_openidconnect/updateForumPassword"
---
# [SoftLayer_User_Customer_OpenIdConnect](/reference/services/SoftLayer_User_Customer_OpenIdConnect)::updateForumPassword

Update a user's forum password


## Overview 
This method is deprecated! SoftLayer Community Forums no longer exist, therefore, this method will return false. In the future, this method will be completely removed. 

Update a user's password on the SoftLayer community forums. As with portal passwords, user forum passwords must match the following restrictions. Forum passwords must... 
* ...be over eight characters long.
* ...be under twenty characters long.
* ...contain at least one uppercase letter
* ...contain at least one lowercase letter
* ...contain at least one number
* ...contain one of the special characters _ - | @ . , ? / ! ~ # $ % ^ & * ( ) { } [ ] \ + =
* ...not match your username
* ...not match your portal password
Finally, users can only update their own password. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|password| string| Your new forum password|


### Required Headers
* authenticate
* SoftLayer_User_Customer_OpenIdConnectInitParameters


### Return Values
* void


### Associated Methods

*  [SoftLayer_User_Customer::updatePassword](/reference/services/SoftLayer_User_Customer/updatePassword )



### Error Handling

* SoftLayer_Exception_Public 

> Throw the exception 'Access is denied.' if a user tries to change another user's forum password. 

* SoftLayer_Exception_Public 

> Throw the exception "Your portal password must" followed by a list of violated password rules if the given password fails to match any of the above restrictions. 

* SoftLayer_Exception_Public 

> Throw the exception "This user does not have a corresponding forum user." if the current user does not have a corresponding user in the SoftLayer community forums. If you recieve this error then please contact support to add your forum user. 



