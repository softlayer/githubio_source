---
title: "assignNewParentId"
description: "This method can be used in place of [SoftLayer_User_Customer::editObject](/reference/datatypes/$1/#$2) to change the parent user of this user. 

The new parent must be a user on the same account, and must not be a child of this user.  A user is not allowed to change their own parent. 

If the cascadeFlag is set to false, then an exception will be thrown if the new parent does not have all of the permissions that this user possesses.  If the cascadeFlag is set to true, then permissions will be removed from this user and the descendants of this user as necessary so that no children of the parent will have permissions that the parent does not possess. However, setting the cascadeFlag to true will not remove the access all device permissions from this user. The customer portal will need to be used to remove these permissions. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_OpenIdConnect_TrustedProfile"
type: "reference"
layout: "method"
mainService : "SoftLayer_User_Customer_OpenIdConnect_TrustedProfile"
---
