---
title: "removeResourceObject"
description: "Unlinks a SoftLayer_Hardware_Server, SoftLayer_Virtual_Guest, or SoftLayer_Virtual_DedicatedHost object from the group."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Permission_Group"
aliases:
    - "/reference/services/softlayer_user_permission_group/removeResourceObject"
---
# [SoftLayer_User_Permission_Group](/reference/services/SoftLayer_User_Permission_Group)::removeResourceObject

Unlinks a hardware, virtual guest, or dedicated host object on the


## Overview 
Unlinks a SoftLayer_Hardware_Server, SoftLayer_Virtual_Guest, or SoftLayer_Virtual_DedicatedHost object from the group. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|resourceObject| <a href='/reference/datatypes/SoftLayer_Entity'>SoftLayer_Entity </a>| The resource record to remove from this group (typically hardware, virtual guest, or dedicated host). See [[SoftLayer_User_Permission_Resource_Type (type)]] for the valid entities for this request.|
|resourceTypeKeyName| string| An optional keyname specifying the type of resource provided. See [[SoftLayer_User_Permission_Resource_Type (type)]] for the valid entities for this request.|


### Required Headers
* authenticate
* SoftLayer_User_Permission_GroupInitParameters


### Return Values
* boolean


### Associated Methods

*  [SoftLayer_User_Permission_Group::addResourceObject](/reference/services/SoftLayer_User_Permission_Group/addResourceObject )



### Error Handling

* SoftLayer_Exception_PermissionDenied 

> Throws the exception "Can't remove resource object to group: Permission Denied." if a customer user attempts this request without the proper permission. 

* SoftLayer_Exception 

> Throws the exception "A permission resource type does not exist for" if one of the object is not one of the valid resource types. 



