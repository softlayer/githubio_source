---
title: "getAllFiles"
description: "{{CloudLayerOnlyMethod}} Retrieve details such as id, name, size, create date for all files in a Storage account's root... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage"
aliases:
    - "/reference/services/softlayer_network_storage/getAllFiles"
---
# [SoftLayer_Network_Storage](/reference/services/SoftLayer_Network_Storage)::getAllFiles

Retrieve a listing of all files in a Storage account's root directory.


## Overview 
{{CloudLayerOnlyMethod}} Retrieve details such as id, name, size, create date for all files in a Storage account's root directory. This does not download file content. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Network_StorageInitParameters


### Optional Headers
* resultLimit

### Return Values
* <a href='/reference/datatypes/SoftLayer_Container_Utility_File_Entity'>SoftLayer_Container_Utility_File_Entity[] </a>


### Associated Methods

*  [SoftLayer_Network_Storage::getFileByIdentifier](/reference/services/SoftLayer_Network_Storage/getFileByIdentifier )
*  [SoftLayer_Network_Storage::downloadFile](/reference/services/SoftLayer_Network_Storage/downloadFile )



### Error Handling

* SoftLayer_Exception_Public 

> Throw the exception "Not yet implemented for this Storage type." if the Storage type is not supported. 



