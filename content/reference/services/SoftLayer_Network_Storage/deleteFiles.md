---
title: "deleteFiles"
description: "{{CloudLayerOnlyMethod}} Delete multiple files within a Storage account. Depending on the type of Storage account, Delet... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage"
---
# [SoftLayer_Network_Storage](/reference/services/SoftLayer_Network_Storage)::deleteFiles

Delete multiple files within a Storage account.


## Overview 
{{CloudLayerOnlyMethod}} Delete multiple files within a Storage account. Depending on the type of Storage account, Deleting either deletes files permanently or sends files to your account's recycle bin. 

Currently, Virtual Server storage is the only type of Storage account that sends files to a recycle bin when deleted. When called against a Virtual Server storage account , this method also determines if the files are in the account's recycle bin. If the files exist in the recycle bin, then they are permanently deleted. 

Please note, files can not be restored once they are permanently deleted. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|fileIds| array of strings| The id or guids of the files you wish to delete.|


### Required Headers
* authenticate
* SoftLayer_Network_StorageInitParameters

### Optional Headers

### Return Values
boolean


### associatedMethods

*  [SoftLayer_Network_Storage::deleteFile](/reference/services/SoftLayer_Network_Storage/deleteFile )
*  [SoftLayer_Network_Storage::deleteAllFiles](/reference/services/SoftLayer_Network_Storage/deleteAllFiles )
*  [SoftLayer_Network_Storage::restoreFile](/reference/services/SoftLayer_Network_Storage/restoreFile )
*  [SoftLayer_Network_Storage::getFilesPendingDelete](/reference/services/SoftLayer_Network_Storage/getFilesPendingDelete )
*  [SoftLayer_Network_Storage::getFilePendingDeleteCount](/reference/services/SoftLayer_Network_Storage/getFilePendingDeleteCount )

