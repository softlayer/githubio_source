---
title: "getByUsername"
description: "Retrieve network storage accounts by username and storage account type. Use this method if you wish to retrieve a storag... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Backup_Evault"
aliases:
    - "/reference/services/softlayer_network_storage_backup_evault/getByUsername"
---
# [SoftLayer_Network_Storage_Backup_Evault](/reference/services/SoftLayer_Network_Storage_Backup_Evault)::getByUsername

Retrieve network storage accounts by username. 


## Overview 
Retrieve network storage accounts by username and storage account type. Use this method if you wish to retrieve a storage record by username rather than by id. The ''type'' parameter must correspond to one of the available ''nasType'' values in the SoftLayer_Network_Storage data type. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|username| string| The full username you wish to search for.|
|type| string| The type of storage accounts you wish to search.|


### Required Headers
* authenticate

### Optional Headers
* SoftLayer_Network_Storage_Backup_EvaultObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage[] </a>


### associatedMethods

*  [SoftLayer_Network_Storage::getObject](/reference/services/SoftLayer_Network_Storage/getObject )

