---
title: "createObject"
description: "Create a new user in the SoftLayer customer portal. It is not possible to set up SLL enable flags during object creation... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_OpenIdConnect"
aliases:
    - "/reference/services/softlayer_user_customer_openidconnect/createObject"
---
# [SoftLayer_User_Customer_OpenIdConnect](/reference/services/SoftLayer_User_Customer_OpenIdConnect)::createObject


Create a new user record.


## Overview 
Create a new user in the SoftLayer customer portal. It is not possible to set up SLL enable flags during object creation. These flags are ignored during object creation. You will need to make a subsequent call to edit object in order to enable VPN access. 

An account's master user and sub-users who have the User Manage permission can add new users. 

Users are created with a default permission set. After adding a user it may be helpful to set their permissions and device access. 

secondaryPasswordTimeoutDays will be set to the system configured default value if the attribute is not provided or the attribute is not a valid value. 

Note, neither password nor vpnPassword parameters are required. 

Password When a new user is created, an email will be sent to the new user's email address with a link to a url that will allow the new user to create or change their password for the SoftLayer customer portal. 

If the password parameter is provided and is not null, then that value will be validated. If it is a valid password, then the user will be created with this password.  This user will still receive a portal password email.  It can be used within 24 hours to change their password, or it can be allowed to expire, and the password provided during user creation will remain as the user's password. 

If the password parameter is not provided or the value is null, the user must set their portal password using the link sent in email within 24 hours.  If the user fails to set their password within 24 hours, then a non-master user can use the "Reset Password" link on the login page of the portal to request a new email.  A master user can use the link to retrieve a phone number to call to assist in resetting their password. 

The password parameter is ignored for VPN_ONLY users or for IBMid authenticated users. 

vpnPassword If the vpnPassword is provided, then the user's vpnPassword will be set to the provided password.  When creating a vpn only user, the vpnPassword MUST be supplied.  If the vpnPassword is not provided, then the user will need to use the portal to edit their profile and set the vpnPassword. 

IBMid considerations When a SoftLayer account is linked to a Platform Services (PaaS, formerly Bluemix) account, AND the trait on the SoftLayer Account indicating IBMid authentication is set, then SoftLayer will delegate the creation of an ACTIVE user to PaaS. This means that even though the request to create a new user in such an account may start at the IMS API, via this delegation we effectively turn it into a request that is driven by PaaS. In particular this means that any "invitation email" that comes to the user, will come from PaaS, not from IMS via IBMid. 

Users created in states other than ACTIVE (for example, a VPN_ONLY user) will be created directly in IMS without delegation (but note that no invitation is sent for a user created in any state other than ACTIVE). 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|templateObject| <a href='/reference/datatypes/SoftLayer_User_Customer_OpenIdConnect'>SoftLayer_User_Customer_OpenIdConnect </a>| The SoftLayer_User_Customer_OpenIdConnect object that you wish to create.|
|password| string| The new user's password.|
|vpnPassword| string| The new user's VPN password.|


### Required Headers
* authenticate


### Optional Headers
* SoftLayer_User_Customer_OpenIdConnectObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_User_Customer_OpenIdConnect'>SoftLayer_User_Customer_OpenIdConnect </a>




