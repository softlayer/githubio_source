---
title: "getFilePendingDeleteCount"
description: "{{CloudLayerOnlyMethod}} Retrieve the number of files pending deletion in a Storage account's recycle bin. Files in an a... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage"
aliases:
    - "/reference/services/softlayer_network_storage/getFilePendingDeleteCount"
---
# [SoftLayer_Network_Storage](/reference/services/SoftLayer_Network_Storage)::getFilePendingDeleteCount

Retrieve the number of files pending deletion in a Storage account's recycle bin.


## Overview 
{{CloudLayerOnlyMethod}} Retrieve the number of files pending deletion in a Storage account's recycle bin. Files in an account's recycle bin may either be restored to the account's root directory or permanently deleted. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Network_StorageInitParameters


### Return Values
* integer


### Associated Methods

*  [SoftLayer_Network_Storage::getRecycleBinFileByIdentifier](/reference/services/SoftLayer_Network_Storage/getRecycleBinFileByIdentifier )
*  [SoftLayer_Network_Storage::getFilesPendingDelete](/reference/services/SoftLayer_Network_Storage/getFilesPendingDelete )
*  [SoftLayer_Network_Storage::getFileCount](/reference/services/SoftLayer_Network_Storage/getFileCount )



### Error Handling

* SoftLayer_Exception_Public 

> Throw the exception "Not yet implemented for this Storage type." if the Storage type is not supported. 



