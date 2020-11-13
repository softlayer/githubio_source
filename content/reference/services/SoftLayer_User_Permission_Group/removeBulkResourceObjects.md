---
title: "removeBulkResourceObjects"
description: ""
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




## Overview 


-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|resourceObjects| <a href='/reference/datatypes/SoftLayer_Entity'>SoftLayer_Entity[] </a>| The resource records to remove from this group.  See [[SoftLayer_User_Permission_Resource_Type (type)]] for the valid entities for this request.|
|resourceTypeKeyName| string| An optional keyname for the type of resource provided. See [[SoftLayer_User_Permission_Resource_Type (type)]] for the valid entities for this request.|


### Required Headers
* authenticate
* SoftLayer_User_Permission_GroupInitParameters


### Return Values
* boolean




