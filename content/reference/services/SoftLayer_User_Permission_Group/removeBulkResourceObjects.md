---
title: "removeBulkResourceObjects"
description: "Unlinks multiple SoftLayer_Hardware_Server, SoftLayer_Virtual_Guest, or SoftLayer_Virtual_DedicatedHost objects from the... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Permission_Group"
aliases:
    - "/reference/services/softlayer_user_permission_group/removeBulkResourceObjects"
---
# [SoftLayer_User_Permission_Group](/reference/services/SoftLayer_User_Permission_Group)::removeBulkResourceObjects

Unlinks multiple account device objects of the same resource type from the group.


## Overview 
Unlinks multiple SoftLayer_Hardware_Server, SoftLayer_Virtual_Guest, or SoftLayer_Virtual_DedicatedHost objects from the group. All objects must be of the same type. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|resourceObjects| <a href='/reference/datatypes/SoftLayer_Entity'>SoftLayer_Entity[] </a>| The resource records to remove from this group (typically hardware, virtual guest, or dedicated host).  See [[SoftLayer_User_Permission_Resource_Type (type)]] for the valid entities for this request.|
|resourceTypeKeyName| string| An optional keyname for the type of resource provided. See [[SoftLayer_User_Permission_Resource_Type (type)]] for the valid entities for this request.|


### Required Headers
* authenticate
* SoftLayer_User_Permission_GroupInitParameters


### Return Values
* boolean


### Associated Methods

*  [SoftLayer_User_Permission_Group::removeResourceObject](/reference/services/SoftLayer_User_Permission_Group/removeResourceObject )
*  [SoftLayer_User_Permission_Group::addBulkResourceObject](/reference/services/SoftLayer_User_Permission_Group/addBulkResourceObject )




