---
title: "deleteFile"
description: "{{CloudLayerOnlyMethod}} Delete an individual file within a Storage account. Depending on the type of Storage account, D... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage"
---
# [SoftLayer_Network_Storage](/reference/services/SoftLayer_Network_Storage)::deleteFile

Delete an individual file within a Storage account.


## Overview 
{{CloudLayerOnlyMethod}} Delete an individual file within a Storage account. Depending on the type of Storage account, Deleting a file either deletes the file permanently or sends the file to your account's recycle bin. 

Currently, Virtual Server storage is the only type of Storage account that sends files to a recycle bin when deleted. When called against a Virtual Server storage account , this method also determines if the file is in the account's recycle bin. If the file exist in the recycle bin, then it is permanently deleted. 

Please note, a file can not be restored once it is permanently deleted. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|fileId| string| The id or guid of the file you wish to delete.|


### Required Headers
* authenticate
* SoftLayer_Network_StorageInitParameters

### Optional Headers

### Return Values
boolean


### associatedMethods

*  [SoftLayer_Network_Storage::deleteFiles](/reference/services/SoftLayer_Network_Storage/deleteFiles )
*  [SoftLayer_Network_Storage::deleteAllFiles](/reference/services/SoftLayer_Network_Storage/deleteAllFiles )
*  [SoftLayer_Network_Storage::restoreFile](/reference/services/SoftLayer_Network_Storage/restoreFile )
*  [SoftLayer_Network_Storage::getFilesPendingDelete](/reference/services/SoftLayer_Network_Storage/getFilesPendingDelete )
*  [SoftLayer_Network_Storage::getFilePendingDeleteCount](/reference/services/SoftLayer_Network_Storage/getFilePendingDeleteCount )

