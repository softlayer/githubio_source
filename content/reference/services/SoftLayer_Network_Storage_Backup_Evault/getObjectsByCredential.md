---
title: "getObjectsByCredential"
description: "Retrieve network storage accounts by SoftLayer_Network_Storage_Credential object. Use this method if you wish to retriev... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Backup_Evault"
aliases:
    - "/reference/services/softlayer_network_storage_backup_evault/getObjectsByCredential"
---
# [SoftLayer_Network_Storage_Backup_Evault](/reference/services/SoftLayer_Network_Storage_Backup_Evault)::getObjectsByCredential

Retrieve network storage accounts by SoftLayer_Network_Storage_Credential object. 


## Overview 
Retrieve network storage accounts by SoftLayer_Network_Storage_Credential object. Use this method if you wish to retrieve a storage record by a credential rather than by id. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|credentialObject| <a href='/reference/datatypes/SoftLayer_Network_Storage_Credential'>SoftLayer_Network_Storage_Credential </a>| |


### Required Headers
* authenticate

### Optional Headers
* SoftLayer_Network_Storage_Backup_EvaultObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage[] </a>

