---
title: "updateVpnPassword"
description: "Update a user's VPN password on the SoftLayer customer portal. As with portal passwords, VPN passwords must match the fo... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_OpenIdConnect"
aliases:
    - "/reference/services/softlayer_user_customer_openidconnect/updateVpnPassword"
---
# [SoftLayer_User_Customer_OpenIdConnect](/reference/services/SoftLayer_User_Customer_OpenIdConnect)::updateVpnPassword

Update a user's VPN password


## Overview 
Update a user's VPN password on the SoftLayer customer portal. As with portal passwords, VPN passwords must match the following restrictions. VPN passwords must... 
* ...be over eight characters long.
* ...be under twenty characters long.
* ...contain at least one uppercase letter
* ...contain at least one lowercase letter
* ...contain at least one number
* ...contain one of the special characters _ - | @ . , ? / ! ~ # $ % ^ & * ( ) { } [ ] \ =
* ...not match your username
* ...not match your forum password
Finally, users can only update their own VPN password. An account's master user can update any of their account users' VPN passwords. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|password| string| Your new VPN password|


### Required Headers
* authenticate
* SoftLayer_User_Customer_OpenIdConnectInitParameters


### Return Values
* boolean

### External Links


* [The SoftLayer Customer Portal](https://manage.softlayer.com)



### Associated Methods

*  [SoftLayer_User_Customer::updatePassword](/reference/services/SoftLayer_User_Customer/updatePassword )



### Error Handling

* SoftLayer_Exception_Public 

> Throw the exception "Access is denied." if a user tries to change another user's VPN password and is not the account's master user. 

* SoftLayer_Exception_Public 

> Throw the exception "Your VPN password must" followed by a list of violated password rules if the given password fails to match any of the above restrictions. 



