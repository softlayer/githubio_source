---
title: "assignNewParentId"
description: "This method can be used in place of [SoftLayer_User_Customer::editObject]({{<ref 'reference/services/SoftLayer_User_Cust... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_OpenIdConnect_TrustedProfile"
aliases:
    - "/reference/services/softlayer_user_customer_openidconnect_trustedprofile/assignNewParentId"
---
# [SoftLayer_User_Customer_OpenIdConnect_TrustedProfile](/reference/services/SoftLayer_User_Customer_OpenIdConnect_TrustedProfile)::assignNewParentId


Assign a different parent to this user. 


## Overview 
This method can be used in place of [SoftLayer_User_Customer::editObject]({{<ref "reference/services/SoftLayer_User_Customer/editObject">}}) to change the parent user of this user. 

The new parent must be a user on the same account, and must not be a child of this user.  A user is not allowed to change their own parent. 

If the cascadeFlag is set to false, then an exception will be thrown if the new parent does not have all of the permissions that this user possesses.  If the cascadeFlag is set to true, then permissions will be removed from this user and the descendants of this user as necessary so that no children of the parent will have permissions that the parent does not possess. However, setting the cascadeFlag to true will not remove the access all device permissions from this user. The customer portal will need to be used to remove these permissions. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|parentId| integer| The id of a [[SoftLayer_User_Customer]] to be assigned as the parent to the instantiated user|
|cascadePermissionsFlag| boolean| Flag specifying whether remove permissions from the user that are not assigned to the new parent|


### Required Headers
* authenticate
* SoftLayer_User_Customer_OpenIdConnect_TrustedProfileInitParameters


### Optional Headers
* SoftLayer_User_Customer_OpenIdConnect_TrustedProfileObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_User_Customer_OpenIdConnect_TrustedProfile'>SoftLayer_User_Customer_OpenIdConnect_TrustedProfile </a>




