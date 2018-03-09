---
title: "addAllowedHost"
description: "Use this method to attach a SoftLayer_Network_Storage_Allowed_Host object to this group.  This will automatically enable... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Group_Iscsi"
---
# [SoftLayer_Network_Storage_Group_Iscsi](/reference/services/SoftLayer_Network_Storage_Group_Iscsi)::addAllowedHost

Attach a SoftLayer_Network_Storage_Allowed_Host object to this group


## Overview 
Use this method to attach a SoftLayer_Network_Storage_Allowed_Host object to this group.  This will automatically enable access from this host to any SoftLayer_Network_Storage volumes currently attached to this group. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|allowedHost| <a href='/reference/datatypes/SoftLayer_Network_Storage_Allowed_Host'>SoftLayer_Network_Storage_Allowed_Host </a>| |


### Required Headers
* authenticate
* SoftLayer_Network_Storage_Group_IscsiInitParameters

### Optional Headers

### Return Values
boolean

