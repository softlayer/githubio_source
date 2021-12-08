---
title: "addResourceObject"
description: "Links a SoftLayer_Hardware_Server, SoftLayer_Virtual_Guest, or SoftLayer_Virtual_DedicatedHost object to the group."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Permission_Group"
aliases:
    - "/reference/services/softlayer_user_permission_group/addResourceObject"
---
# [SoftLayer_User_Permission_Group](/reference/services/SoftLayer_User_Permission_Group)::addResourceObject


Links a hardware, virtual guest, or dedicated host object on the


## Overview 
Links a SoftLayer_Hardware_Server, SoftLayer_Virtual_Guest, or SoftLayer_Virtual_DedicatedHost object to the group. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|resourceObject| <a href='/reference/datatypes/SoftLayer_Entity'>SoftLayer_Entity </a>| The object of the resource record (typically hardware, virtual guest, or dedicated host) to add to this group.  See [[SoftLayer_User_Permission_Resource_Type (type)]] for the valid entities for this request.|
|resourceTypeKeyName| string| An optional keyname for the type of resource provided.  See [[SoftLayer_User_Permission_Resource_Type (type)]] for the valid entities for this request.|


### Required Headers
* authenticate
* SoftLayer_User_Permission_GroupInitParameters


### Return Values
* boolean


### Associated Methods

*  [SoftLayer_User_Permission_Group::removeResourceObject](/reference/services/SoftLayer_User_Permission_Group/removeResourceObject )



### Error Handling

* SoftLayer_Exception_PermissionDenied 

> Throws the exception "Can't add resource object to group: Permission Denied." if a customer user attempts this request without the proper permission. 

* SoftLayer_Exception 

> Throws the exception "A permission resource type does not exist for" if one of the object is not one of the valid resource types. 

* SoftLayer_Exception_User_Permission_Inaccessible 

> Throws the exception "Resource object id is invalid" if the provided resource object does not contain an id. 



