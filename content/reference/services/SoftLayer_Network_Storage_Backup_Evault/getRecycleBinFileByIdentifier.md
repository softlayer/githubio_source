---
title: "getRecycleBinFileByIdentifier"
description: "{{CloudLayerOnlyMethod}} Retrieve the details of a file that is pending deletion in a Storage account's a recycle bin."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Backup_Evault"
aliases:
    - "/reference/services/softlayer_network_storage_backup_evault/getRecycleBinFileByIdentifier"
---
# [SoftLayer_Network_Storage_Backup_Evault](/reference/services/SoftLayer_Network_Storage_Backup_Evault)::getRecycleBinFileByIdentifier

Retrieve all files that are in the recycle bin (pending delete).  This method is only used for Virtual Server Storage accounts at moment but may expanded to other Storage types in the future.


## Overview 
{{CloudLayerOnlyMethod}} Retrieve the details of a file that is pending deletion in a Storage account's a recycle bin. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|fileId| string| The id or guid of the file to retrieve.|


### Required Headers
* authenticate
* SoftLayer_Network_Storage_Backup_EvaultInitParameters


### Return Values
* <a href='/reference/datatypes/SoftLayer_Container_Utility_File_Entity'>SoftLayer_Container_Utility_File_Entity </a>


### Associated Methods

*  [SoftLayer_Network_Storage::restoreFile](/reference/services/SoftLayer_Network_Storage/restoreFile )
*  [SoftLayer_Network_Storage::deleteFile](/reference/services/SoftLayer_Network_Storage/deleteFile )



### Error Handling

* SoftLayer_Exception_Public 

> Throw the exception "Not yet implemented for this Storage type." if the Storage type is not supported. 



