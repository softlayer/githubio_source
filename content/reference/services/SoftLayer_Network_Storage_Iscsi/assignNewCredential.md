---
title: "assignNewCredential"
description: "This method will set up a new credential for the remote storage volume. The storage volume must support an additional cr... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Iscsi"
---
# SoftLayer_Network_Storage_Iscsi::assignNewCredential
## Overview 
This method will set up a new credential for the remote storage volume. The storage volume must support an additional credential. Once created, the credential will be automatically assigned to the current volume. If there are no volumes assigned to the credential it will be automatically deleted. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|type| string| The type of credential you would like to add to your storage volume, it must be an approved credential type (current types are: 'ISCSI_MASTER_KEY')|


### Required Headers
* authenticate
* SoftLayer_Network_Storage_IscsiInitParameters

### Optional Headers
* SoftLayer_Network_Storage_IscsiObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Network_Storage_Credential'>SoftLayer_Network_Storage_Credential </a>

