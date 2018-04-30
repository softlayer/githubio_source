---
title: "createOrUpdateLunId"
description: "The LUN ID only takes effect during the Host Authorization process. It is required to de-authorize all hosts before usin... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Iscsi"
aliases:
    - "/reference/services/softlayer_network_storage_iscsi/createOrUpdateLunId"
---
# [SoftLayer_Network_Storage_Iscsi](/reference/services/SoftLayer_Network_Storage_Iscsi)::createOrUpdateLunId

Creates or updates the LUN ID property on a volume.


## Overview 
The LUN ID only takes effect during the Host Authorization process. It is required to de-authorize all hosts before using this method. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|lunId| integer| <<< EOT|


### Required Headers
* authenticate
* SoftLayer_Network_Storage_IscsiInitParameters

### Optional Headers
* SoftLayer_Network_Storage_IscsiObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Network_Storage_Property'>SoftLayer_Network_Storage_Property </a>

