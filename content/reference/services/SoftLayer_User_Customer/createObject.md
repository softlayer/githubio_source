---
title: "createObject"
description: "Create a new user in the SoftLayer customer portal. createObject() creates a user's portal record and adds them into the... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer"
---
# [SoftLayer_User_Customer](/reference/services/SoftLayer_User_Customer)::createObject

Create a new user record.


## Overview 
Create a new user in the SoftLayer customer portal. createObject() creates a user's portal record and adds them into the SoftLayer community forums. It is not possible to set up SLL or PPTP enable flags during object creation. These flags are ignored during object creation. You will need to make a subsequent call to edit object in order to enable VPN access. An account's master user and sub-users who have the User Manage permission can add new users. createObject() creates users with a default permission set. After adding a user it may be helpful to set their permissions and hardware access. 

Note, neither password nor vpnPassword parameters are required. 

Password When a new user is created, an email will be sent to the new user's email address with a link to a url that will allow the new user to create or change their password for the SoftLayer customer portal. 

If the password parameter is provided and is not null, then that value will be validated. If it is a valid password, then the user will be created with this password.  This user will still receive a portal password email.  It can be used within 24 hours to change their password, or it can be allowed to expire, and the password provided during user creation will remain as the user's password. 

If the password parameter is not provided or the value is null, the user must set their portal password using the link sent in email within 24 hours.  If the user fails to set their password within 24 hours, then a non-master user can use the "Reset Password" link on the login page of the portal to request a new email.  A master user can use the link to retrieve a phone number to call to assist in resetting their password. 

The password parameter is ignored for VPN_ONLY users or for IBMid authenticated users. 

vpnPassword If the vpnPassword is provided, then the user's vpnPassword will be set to the provided password.  When creating a vpn only user, the vpnPassword MUST be supplied.  If the vpnPassword is not provided, then the user will need to use the portal to edit their profile and set the vpnPassword. 



### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|templateObject| <a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer </a>| The SoftLayer_User_Customer object that you wish to create.|
|password| string| The new user's password.|
|vpnPassword| string| The new user's VPN password.|


### Required Headers
* authenticate

### Optional Headers
* SoftLayer_User_CustomerObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer </a>

