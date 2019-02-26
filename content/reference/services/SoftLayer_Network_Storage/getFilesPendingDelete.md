---
title: "getFilesPendingDelete"
description: "{{CloudLayerOnlyMethod}} Retrieve a list of files that are pending deletion in a Storage account's recycle bin. Files in... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage"
aliases:
    - "/reference/services/softlayer_network_storage/getFilesPendingDelete"
---
# [SoftLayer_Network_Storage](/reference/services/SoftLayer_Network_Storage)::getFilesPendingDelete

Retrieve a list of files in a Storage account's recycle bin.


## Overview 
{{CloudLayerOnlyMethod}} Retrieve a list of files that are pending deletion in a Storage account's recycle bin. Files in an account's recycle bin may either be restored to the account's root directory or permanently deleted. This method does not download file content. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Network_StorageInitParameters


### Return Values
* <a href='/reference/datatypes/SoftLayer_Container_Utility_File_Entity'>SoftLayer_Container_Utility_File_Entity[] </a>


### Associated Methods

*  [SoftLayer_Network_Storage::getAllFiles](/reference/services/SoftLayer_Network_Storage/getAllFiles )
*  [SoftLayer_Network_Storage::getRecycleBinFileByIdentifier](/reference/services/SoftLayer_Network_Storage/getRecycleBinFileByIdentifier )
*  [SoftLayer_Network_Storage::getFilePendingDeleteCount](/reference/services/SoftLayer_Network_Storage/getFilePendingDeleteCount )
*  [SoftLayer_Network_Storage::restoreFile](/reference/services/SoftLayer_Network_Storage/restoreFile )
*  [SoftLayer_Network_Storage::deleteFile](/reference/services/SoftLayer_Network_Storage/deleteFile )



### Error Handling

* SoftLayer_Exception_Public 

> Throw the exception "Not yet implemented for this Storage type." if the Storage type is not supported. 



