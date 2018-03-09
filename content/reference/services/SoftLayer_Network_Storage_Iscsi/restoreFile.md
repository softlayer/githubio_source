---
title: "restoreFile"
description: "{{CloudLayerOnlyMethod}} Restore an individual file so that it may be used as it was before it was deleted. 

If a file... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Iscsi"
---
# [SoftLayer_Network_Storage_Iscsi](/reference/services/SoftLayer_Network_Storage_Iscsi)::restoreFile

Restore access to an individual file in a Storage account.


## Overview 
{{CloudLayerOnlyMethod}} Restore an individual file so that it may be used as it was before it was deleted. 

If a file is deleted from a Virtual Server Storage account, the file is placed into the account's recycle bin and not permanently deleted. Therefore, restoreFile can be used to place the file back into your Virtual Server account's root directory. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|fileId| string| The id or guid of the file you wish to restore.|


### Required Headers
* authenticate
* SoftLayer_Network_Storage_IscsiInitParameters

### Optional Headers

### Return Values
<a href='/reference/datatypes/SoftLayer_Container_Utility_File_Entity'>SoftLayer_Container_Utility_File_Entity </a>


### associatedMethods

*  [SoftLayer_Network_Storage::deleteFile](/reference/services/SoftLayer_Network_Storage/deleteFile )
*  [SoftLayer_Network_Storage::deleteFiles](/reference/services/SoftLayer_Network_Storage/deleteFiles )
*  [SoftLayer_Network_Storage::deleteAllFiles](/reference/services/SoftLayer_Network_Storage/deleteAllFiles )
*  [SoftLayer_Network_Storage::getFilesPendingDelete](/reference/services/SoftLayer_Network_Storage/getFilesPendingDelete )
*  [SoftLayer_Network_Storage::getFilePendingDeleteCount](/reference/services/SoftLayer_Network_Storage/getFilePendingDeleteCount )

