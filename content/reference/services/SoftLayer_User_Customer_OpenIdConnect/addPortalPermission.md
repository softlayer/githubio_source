---
title: "addPortalPermission"
description: "Add a permission to a portal user's permission set. [SoftLayer_User_Customer_CustomerPermission_Permission]({{<ref 'refe... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_OpenIdConnect"
aliases:
    - "/reference/services/softlayer_user_customer_openidconnect/addPortalPermission"
---
# [SoftLayer_User_Customer_OpenIdConnect](/reference/services/SoftLayer_User_Customer_OpenIdConnect)::addPortalPermission

Add a permission to a portal user's permission set.


## Overview 
Add a permission to a portal user's permission set. [SoftLayer_User_Customer_CustomerPermission_Permission]({{<ref "reference/datatypes/SoftLayer_User_Customer_CustomerPermission_Permission">}}) control which features in the SoftLayer customer portal and API a user may use. If the user already has the permission you're attempting to add then addPortalPermission() returns true. 

Users can assign permissions to their child users, but not to themselves. An account's master has all portal permissions and can set permissions for any of the other users on their account. 

Use the [SoftLayer_User_Customer_CustomerPermission_Permission::getAllObjects]({{<ref "reference/services/SoftLayer_User_Customer_CustomerPermission_Permission/getAllObjects">}}) method to retrieve a list of all permissions available in the SoftLayer customer portal and API. Permissions are added based on the keyName property of the permission parameter. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|permission| <a href='/reference/datatypes/SoftLayer_User_Customer_CustomerPermission_Permission'>SoftLayer_User_Customer_CustomerPermission_Permission </a>| The permission you wish to add to the given user.|


### Required Headers
* authenticate
* SoftLayer_User_Customer_OpenIdConnectInitParameters


### Return Values
* boolean


### Associated Methods

*  [SoftLayer_User_Customer::addBulkPortalPermission](/reference/services/SoftLayer_User_Customer/addBulkPortalPermission )
*  [SoftLayer_User_Customer::removePortalPermission](/reference/services/SoftLayer_User_Customer/removePortalPermission )
*  [SoftLayer_User_Customer::removeBulkPortalPermission](/reference/services/SoftLayer_User_Customer/removeBulkPortalPermission )



### Error Handling

* SoftLayer_Exception_Public 

> Throw the exception "You may not add permissions to your account." when trying to add permissions to the user making calling the SoftLayer API. 

* SoftLayer_Exception_Public 

> Throw the exception "You may not add permissions to this account." the user making the API call is not their account's master user or does not have the "Add New User" portal permission. 

* SoftLayer_Exception_Public 

> Throw the exception "Please specify a permission key name." if the keyName property of the permission parameter is empty. 

* SoftLayer_Exception_Public 

> Throw the exception "Unable to locate a permission with the key name {key name}." when trying to assign an unknown permission to a user. 

* SoftLayer_Exception_Public 

> Throw the exception "Unable to add user permission {key name}." if the API was unable to assign the given permission to the given portal user. 



