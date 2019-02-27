---
title: "getFileCount"
description: "{{CloudLayerOnlyMethod}} Retrieve the file number of files in a Virtual Server Storage account's root directory. This do... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Iscsi"
aliases:
    - "/reference/services/softlayer_network_storage_iscsi/getFileCount"
---
# [SoftLayer_Network_Storage_Iscsi](/reference/services/SoftLayer_Network_Storage_Iscsi)::getFileCount

Retrieve the file number of files in a Virtual Server Storage account's root directory.


## Overview 
{{CloudLayerOnlyMethod}} Retrieve the file number of files in a Virtual Server Storage account's root directory. This does not include the files stored in the recycle bin. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Network_Storage_IscsiInitParameters


### Return Values
* integer


### Associated Methods

*  [SoftLayer_Network_Storage::getAllFiles](/reference/services/SoftLayer_Network_Storage/getAllFiles )
*  [SoftLayer_Network_Storage::getFilePendingDeleteCount](/reference/services/SoftLayer_Network_Storage/getFilePendingDeleteCount )



### Error Handling

* SoftLayer_Exception_Public 

> Throw the exception "Not yet implemented for this Storage type." if the Storage type is not supported. 



