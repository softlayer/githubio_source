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
---
# SoftLayer_Network_Storage_Backup_Evault::getRecycleBinFileByIdentifier
## Overview 
{{CloudLayerOnlyMethod}} Retrieve the details of a file that is pending deletion in a Storage account's a recycle bin. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|fileId| string| The id or guid of the file to retrieve.|


### Required Headers
* authenticate
* SoftLayer_Network_Storage_Backup_EvaultInitParameters

### Optional Headers

### Return Values
<a href='/reference/datatypes/SoftLayer_Container_Utility_File_Entity'>SoftLayer_Container_Utility_File_Entity </a>


### associatedMethods

*  [SoftLayer_Network_Storage::restoreFile](/reference/services/SoftLayer_Network_Storage/restoreFile )
*  [SoftLayer_Network_Storage::deleteFile](/reference/services/SoftLayer_Network_Storage/deleteFile )

