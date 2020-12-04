---
title: "addBulkResourceObjects"
description: "Links multiple SoftLayer_Hardware_Server, SoftLayer_Virtual_Guest, or SoftLayer_Virtual_DedicatedHost objects to the gro... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Permission_Group"
aliases:
    - "/reference/services/softlayer_user_permission_group/addBulkResourceObjects"
---
# [SoftLayer_User_Permission_Group](/reference/services/SoftLayer_User_Permission_Group)::addBulkResourceObjects

Links multiple account device objects of the same resource type to the group.


## Overview 
Links multiple SoftLayer_Hardware_Server, SoftLayer_Virtual_Guest, or SoftLayer_Virtual_DedicatedHost objects to the group. All objects must be of the same type. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|resourceObjects| <a href='/reference/datatypes/SoftLayer_Entity'>SoftLayer_Entity[] </a>| The resource records to add to this group. See [[SoftLayer_User_Permission_Resource_Type (type)]] for the valid entities for this request.|
|resourceTypeKeyName| string| An optional keyname for the type of resources provided.  See [[SoftLayer_User_Permission_Resource_Type (type)]] for the valid entities for this request.|


### Required Headers
* authenticate
* SoftLayer_User_Permission_GroupInitParameters


### Return Values
* boolean


### Associated Methods

*  [SoftLayer_User_Permission_Group::addResourceObject](/reference/services/SoftLayer_User_Permission_Group/addResourceObject )
*  [SoftLayer_User_Permission_Group::removeBulkResourceObject](/reference/services/SoftLayer_User_Permission_Group/removeBulkResourceObject )




