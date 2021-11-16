---
title: "addBulkPortalPermission"
description: "Add multiple permissions to a portal user's permission set. [SoftLayer_User_Customer_CustomerPermission_Permission]({{<r... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_OpenIdConnect"
aliases:
    - "/reference/services/softlayer_user_customer_openidconnect/addBulkPortalPermission"
---
# [SoftLayer_User_Customer_OpenIdConnect](/reference/services/SoftLayer_User_Customer_OpenIdConnect)::addBulkPortalPermission


Add multiple permissions to a portal user's permission set.


## Overview 
Add multiple permissions to a portal user's permission set. [SoftLayer_User_Customer_CustomerPermission_Permission]({{<ref "reference/datatypes/SoftLayer_User_Customer_CustomerPermission_Permission">}}) control which features in the SoftLayer customer portal and API a user may use. addBulkPortalPermission() does not attempt to add permissions already assigned to the user. 

Users can assign permissions to their child users, but not to themselves. An account's master has all portal permissions and can set permissions for any of the other users on their account. 

Use the [SoftLayer_User_Customer_CustomerPermission_Permission::getAllObjects]({{<ref "reference/services/SoftLayer_User_Customer_CustomerPermission_Permission/getAllObjects">}}) method to retrieve a list of all permissions available in the SoftLayer customer portal and API. Permissions are removed based on the keyName property of the permission objects within the permissions parameter. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|permissions| <a href='/reference/datatypes/SoftLayer_User_Customer_CustomerPermission_Permission'>SoftLayer_User_Customer_CustomerPermission_Permission[] </a>| A collection of permissions to assign to this user.|


### Required Headers
* authenticate
* SoftLayer_User_Customer_OpenIdConnectInitParameters


### Return Values
* boolean


### Associated Methods

*  [SoftLayer_User_Customer::addPortalPermission](/reference/services/SoftLayer_User_Customer/addPortalPermission )
*  [SoftLayer_User_Customer::removePortalPermission](/reference/services/SoftLayer_User_Customer/removePortalPermission )
*  [SoftLayer_User_Customer::removeBulkPortalPermission](/reference/services/SoftLayer_User_Customer/removeBulkPortalPermission )



### Error Handling

* SoftLayer_Exception_Public 

> Throws the exception "You may not add permissions to your account." when trying to add permissions to the user making calling the SoftLayer API. 

* SoftLayer_Exception_Public 

> Throws the exception "Please specify a permission key name." if the keyName property of the permission parameter is empty. 

* SoftLayer_Exception_Public 

> Throws the exception "Unable to locate a permission with the key name {key name}." when trying to assign an unknown permission to a user. 

* SoftLayer_Exception_Public 

> Throws the exception "Unable to add user permission {key name}." if the API was unable to assign the given permission to the given portal user. 



